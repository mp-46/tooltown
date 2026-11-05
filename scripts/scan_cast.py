import struct

def scan_file(filepath):
    print("=== Scanning:", filepath)
    with open(filepath, 'rb') as f:
        # Check RIFX / MV93
        sig = f.read(4)
        if sig != b'RIFX':
            print("Not RIFX")
            return
        size = struct.unpack('>I', f.read(4))[0]
        ver = f.read(4)
        imap_tag = f.read(4)
        imap_len = struct.unpack('>I', f.read(4))[0]
        imap_data = f.read(imap_len)
        mmap_offset = struct.unpack('>I', imap_data[4:8])[0]
        
        # Read mmap
        f.seek(mmap_offset)
        m_tag = f.read(4)
        m_len = struct.unpack('>I', f.read(4))[0]
        m_hdr = f.read(24)
        hdr_len, entry_len, max_entries, used_entries = struct.unpack('>HHII', m_hdr[:12])
        print(f"Header: hdr_len={hdr_len}, entry_len={entry_len}, max={max_entries}, used={used_entries}")
        
        chunks = []
        for i in range(used_entries):
            e = f.read(entry_len)
            tag = e[:4].decode('latin1', errors='replace')
            length, offset = struct.unpack('>II', e[4:12])
            chunks.append((i, tag, length, offset))
        
        # Read KEY*
        key_map = {} # cast_idx -> list of (res_idx, fourcc)
        for i, tag, length, offset in chunks:
            if tag == 'KEY*':
                f.seek(offset + 8)
                khdr = f.read(12)
                entry_num = struct.unpack('>H', khdr[6:8])[0]
                total_entries = (length - 12) // 12
                for k in range(total_entries):
                    kentry = f.read(12)
                    if len(kentry) < 12: break
                    res_idx, cast_idx = struct.unpack('>II', kentry[:8])
                    fourcc = kentry[8:12].decode('latin1', errors='replace')
                    if cast_idx not in key_map:
                        key_map[cast_idx] = []
                    key_map[cast_idx].append((res_idx, fourcc))
        
        # Scan CASt
        for i, tag, length, offset in chunks:
            if tag == 'CASt':
                f.seek(offset + 8)
                data = f.read(length)
                top, left, bottom, right = struct.unpack('>4h', data[10:18])
                w, h = right - left, bottom - top
                # Extract trailing name if any
                name = ""
                for j in range(len(data) - 1, 0, -1):
                    if data[j] < 32 or data[j] > 126:
                        if len(data) - 1 - j >= 2:
                            name = data[j+1:].decode('latin1', errors='replace')
                            break
                linked = key_map.get(i, [])
                linked_str = ", ".join(f"{fc}@{r}" for r, fc in linked)
                print(f"Cast {i:3d}: size=({w:4d}x{h:4d}) rect=({top},{left},{bottom},{right}) linked=[{linked_str}] name='{name}'")

if __name__ == '__main__':
    scan_file(r'tooltown_extracted\AD\MOD01\MAP.DIR')
