Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)
WshShell.CurrentDirectory = scriptDir & "\game"

exePath = """" & scriptDir & "\otvdm\otvdmw.exe"""
manualPath = """" & scriptDir & "\game\TTMANUAL.EXE"""

WshShell.Run exePath & " " & manualPath, 0, False

