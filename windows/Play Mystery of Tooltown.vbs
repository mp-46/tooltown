Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)
WshShell.CurrentDirectory = scriptDir & "\game"

exePath = """" & scriptDir & "\otvdm\otvdmw.exe"""
gamePath = """" & scriptDir & "\game\TOOL.EXE"""

WshShell.Run exePath & " " & gamePath, 0, False

