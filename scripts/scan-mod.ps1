#Requires -Version 5.1
<#
.SYNOPSIS
  Windows convenience wrapper around scripts/scan_mod.py.
.EXAMPLE
  ./scripts/scan-mod.ps1 mods/1.20.1/technom-1.20.1-0.1.0-dev.jar
.EXAMPLE
  ./scripts/scan-mod.ps1 --all
#>
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Args
)

$ErrorActionPreference = 'Stop'
$py = (Get-Command python -ErrorAction SilentlyContinue)
if (-not $py) { $py = Get-Command py -ErrorAction SilentlyContinue }
if (-not $py) { throw 'Python not found. Install Python 3.9+ and retry.' }

$script = Join-Path $PSScriptRoot 'scan_mod.py'
& $py.Source $script @Args
exit $LASTEXITCODE
