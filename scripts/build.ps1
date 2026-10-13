#Requires -Version 5.1
<#
.SYNOPSIS
  Rebuild catalog + README (and optionally validate) with one command.
.EXAMPLE
  ./scripts/build.ps1
.EXAMPLE
  ./scripts/build.ps1 -Validate
#>
param(
    [switch]$Validate
)

$ErrorActionPreference = 'Stop'
$py = (Get-Command python -ErrorAction SilentlyContinue)
if (-not $py) { $py = Get-Command py -ErrorAction SilentlyContinue }
if (-not $py) { throw 'Python not found. Install Python 3.9+ and retry.' }

& $py.Source (Join-Path $PSScriptRoot 'build_catalog.py')
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& $py.Source (Join-Path $PSScriptRoot 'gen_readme.py')
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
if ($Validate) {
    & $py.Source (Join-Path $PSScriptRoot 'validate.py') --check-generated
    exit $LASTEXITCODE
}
exit 0
