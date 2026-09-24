$ErrorActionPreference = 'Stop'
$ProjectRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$PythonExe = Join-Path $ProjectRoot '.venv/Scripts/python.exe'
if (-not (Test-Path -LiteralPath $PythonExe)) { $PythonExe = 'python' }
& $PythonExe (Join-Path $PSScriptRoot 'launch.py') login
if ($LASTEXITCODE -ne 0) { throw 'DataAnalyser login failed.' }
