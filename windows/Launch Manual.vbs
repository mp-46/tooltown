Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)
WshShell.CurrentDirectory = scriptDir & "\game"

exePath = """" & scriptDir & "\otvdm\otvdmw.exe"""

WshShell.Run exePath & " TTMANUAL.EXE", 0, False

