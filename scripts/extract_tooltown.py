import os
import struct
from PIL import Image

def unpack_bitd(stream_bytes, w, h, bpp=8):
    pixels = bytearray()
    idx = 0
    total = len(stream_bytes)
    bytes_need = w * h * bpp // 8
    
    if total == bytes_need:
        pixels = bytearray(stream_bytes)
    else:
        while idx < total:
            data = stream_bytes[idx]
            idx += 1
            if (data & 0x80) != 0:
                length = ((data ^ 0xFF) & 0xFF) + 2
                if idx < total:
                    val = stream_bytes[idx]
                    idx += 1
                    pixels.extend([val] * length)
            else:
                length = data + 1
                end = min(idx + length, total)
                pixels.extend(stream_bytes[idx:end])
                idx = end

    if len(pixels) < bytes_need:
        pixels.extend([0] * (bytes_need - len(pixels)))

    offset = w % 2 if bpp == 8 else 0
    out_img = Image.new('P' if bpp == 8 else '1', (w, h))
    out_pixels = bytearray(w * h)
    
    if bpp == 8:
        for y in range(h):
            row_start = (y * w) + (y * offset)
            for x in range(w):
                if row_start + x < len(pixels):
                    out_pixels[y * w + x] = pixels[row_start + x]
        out_img.frombytes(bytes(out_pixels))
    elif bpp == 1:
        pitch = (w + 7) // 8
        for y in range(h):
            for x in range(w):
                byte_val = pixels[y * pitch + (x >> 3)]
                bit = (byte_val & (1 << (7 - (x & 7)))) != 0
                out_pixels[y * w + x] = 255 if bit else 0
        out_img = Image.frombytes('L', (w, h), bytes(out_pixels)).convert('1')

    return out_img

def extract_dir(dir_path, output_dir, palette_img):
    os.makedirs(output_dir, exist_ok=True)
    if not os.path.exists(dir_path):
        print(f"File not found: {dir_path}")
        return 0
    with open(dir_path, 'rb') as f:
        sig = f.read(4)
        if sig != b'RIFX': return 0
        f.seek(12)
        f.read(4) # imap
        imap_len = struct.unpack('>I', f.read(4))[0]
        imap_data = f.read(imap_len)
        mmap_offset = struct.unpack('>I', imap_data[4:8])[0]
        
        f.seek(mmap_offset)
        f.read(8)
        m_hdr = f.read(24)
        hdr_len, entry_len, max_entries, used_entries = struct.unpack('>HHII', m_hdr[:12])
        
        chunks = []
        for i in range(used_entries):
            e = f.read(entry_len)
            tag = e[:4].decode('latin1', errors='replace')
            length, offset = struct.unpack('>II', e[4:12])
            chunks.append((i, tag, length, offset))
            
        key_map = {}
        for i, tag, length, offset in chunks:
            if tag == 'KEY*':
                f.seek(offset + 8)
                khdr = f.read(12)
                total_entries = (length - 12) // 12
                for k in range(total_entries):
                    kentry = f.read(12)
                    if len(kentry) < 12: break
                    res_idx, cast_idx = struct.unpack('>II', kentry[:8])
                    fourcc = kentry[8:12].decode('latin1', errors='replace')
                    if cast_idx not in key_map:
                        key_map[cast_idx] = []
                    key_map[cast_idx].append((res_idx, fourcc))
                    
        count = 0
        for i, tag, length, offset in chunks:
            if tag == 'CASt':
                f.seek(offset + 8)
                cdata = f.read(length)
                top, left, bottom, right = struct.unpack('>4h', cdata[10:18])
                w, h = right - left, bottom - top
                bpp = cdata[31] if len(cdata) > 31 else 8
                if bpp == 0: bpp = 8
                
                name = ""
                for j in range(len(cdata) - 1, 0, -1):
                    if cdata[j] < 32 or cdata[j] > 126:
                        if len(cdata) - 1 - j >= 2:
                            name = cdata[j+1:].decode('latin1', errors='replace')
                            break
                            
                linked = key_map.get(i, [])
                for res_idx, fourcc in linked:
                    if fourcc == 'BITD' and w > 0 and h > 0:
                        bchunk = chunks[res_idx]
                        f.seek(bchunk[3] + 8)
                        bdata = f.read(bchunk[2])
                        img = unpack_bitd(bdata, w, h, bpp)
                        if bpp == 8 and palette_img.palette:
                            img.palette = palette_img.palette
                        safe_name = "".join(c for c in name if c.isalnum() or c in (' ', '_', '-')).strip()
                        if not safe_name: safe_name = f"cast_{i}"
                        fname = f"{i:03d}_{safe_name}.png"
                        out_path = os.path.join(output_dir, fname)
                        img.save(out_path)
                        count += 1
                    elif fourcc == 'snd ':
                        schunk = chunks[res_idx]
                        f.seek(schunk[3] + 8)
                        sdata = f.read(schunk[2])
                        safe_name = "".join(c for c in name if c.isalnum() or c in (' ', '_', '-')).strip()
                        if not safe_name: safe_name = f"cast_{i}"
                        fname = f"{i:03d}_{safe_name}.wav"
                        out_path = os.path.join(output_dir, fname)
                        import wave
                        with wave.open(out_path, 'wb') as wav:
                            wav.setnchannels(1)
                            wav.setsampwidth(1)
                            wav.setframerate(22050)
                            wav.writeframes(sdata)
                        count += 1
                        
    print(f"Extracted {count} assets from {os.path.basename(dir_path)} -> {output_dir}")
    return count

if __name__ == '__main__':
    pal_img = Image.open(r'tooltown_extracted\TOOL.BMP')
    
    targets = [
        (r'tooltown_extracted\AD\ADOPEN.DIR', r'games\tooltown\assets\intro'),
        (r'tooltown_extracted\AD\BACKPACK.DIR', r'games\tooltown\assets\backpack'),
        (r'tooltown_extracted\AD\MOD01\CITY1.DIR', r'games\tooltown\assets\city'),
        (r'tooltown_extracted\AD\MOD01\OHOUSE.DIR', r'games\tooltown\assets\ohouse'),
        (r'tooltown_extracted\AD\MOD01\GROSTO.DIR', r'games\tooltown\assets\grosto'),
        (r'tooltown_extracted\AD\MOD01\SHOP\HARDWARE.DIR', r'games\tooltown\assets\hardware'),
        (r'tooltown_extracted\AD\MOD01\SHOP\MALL.DIR', r'games\tooltown\assets\mall'),
        (r'tooltown_extracted\AD\MOD01\UNIV\LOB.DIR', r'games\tooltown\assets\univ'),
        (r'tooltown_extracted\AD\MOD01\MUS\MLOB.DIR', r'games\tooltown\assets\mus'),
    ]
    
    total = 0
    for src, dst in targets:
        total += extract_dir(src, dst, pal_img)
    print(f"DONE! Total extracted assets across all main scenes: {total}")
