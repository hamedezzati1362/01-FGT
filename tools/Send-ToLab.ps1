<#
.SYNOPSIS
  Send a file from this PC to ESXi or PNetLab via scp, then verify SHA256.
.DESCRIPTION
  - Does NOT store passwords (scp/ssh will prompt you).
  - Asks before overwriting.
  - Requires Windows OpenSSH client (ssh.exe, scp.exe).
  UNTESTED draft: try with a small file first.
.EXAMPLE
  .\Send-ToLab.ps1 -Path .\Win2022.iso -Target EsxiIso
  .\Send-ToLab.ps1 -Path .\virtioa.qcow2 -Target PnetImage -ImageFolder fortinet-7.0.3
#>
param(
  [Parameter(Mandatory=$true)][string]$Path,
  [Parameter(Mandatory=$true)][ValidateSet('EsxiIso','PnetImage','PnetLabs')][string]$Target,
  [string]$ImageFolder = '',
  [string]$EsxiHost = '192.168.88.3',
  [string]$PnetHost = '192.168.88.199',
  [string]$User = 'root'
)
$ErrorActionPreference = 'Stop'
if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) { throw "File not found: $Path" }
$file = Get-Item -LiteralPath $Path
$name = $file.Name

switch ($Target) {
  'EsxiIso'   { $hostName = $EsxiHost; $remoteDir = '/vmfs/volumes/ds01-ssd/iso' }
  'PnetLabs'  { $hostName = $PnetHost; $remoteDir = '/opt/unetlab/labs' }
  'PnetImage' {
      if ([string]::IsNullOrWhiteSpace($ImageFolder)) { throw "-ImageFolder is required for PnetImage (e.g. fortinet-7.0.3)" }
      $hostName = $PnetHost; $remoteDir = "/opt/unetlab/addons/qemu/$ImageFolder"
  }
}
$remotePath = "$remoteDir/$name"
$dest = "$User@$hostName"

Write-Host "Local : $($file.FullName)  ($([math]::Round($file.Length/1MB,1)) MB)"
Write-Host "Remote: ${dest}:${remotePath}"
$localHash = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash.ToLower()
Write-Host "Local SHA256: $localHash"

# make sure remote dir exists, and warn if file exists
$exists = & ssh $dest "mkdir -p '$remoteDir' && [ -e '$remotePath' ] && echo EXISTS || echo NEW"
if ($exists -match 'EXISTS') {
  $ans = Read-Host "Remote file exists. Overwrite? (y/N)"
  if ($ans -ne 'y') { Write-Host "Cancelled."; exit 1 }
}

& scp $file.FullName "${dest}:${remotePath}"
if ($LASTEXITCODE -ne 0) { throw "scp failed" }

$remoteOut = & ssh $dest "sha256sum '$remotePath'"
$remoteHash = ($remoteOut -split '\s+')[0].ToLower()
Write-Host "Remote SHA256: $remoteHash"
if ($remoteHash -eq $localHash) { Write-Host "OK: hashes match." -ForegroundColor Green }
else { Write-Host "MISMATCH! Copy is not identical. Delete it and retry." -ForegroundColor Red; exit 2 }

if ($Target -eq 'PnetImage') {
  $ans = Read-Host "Run PNetLab fixpermissions now? (y/N)"
  if ($ans -eq 'y') { & ssh $dest "/opt/unetlab/wrappers/unl_wrapper -a fixpermissions" }
}
