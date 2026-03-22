param (
    [string]$Root = ".",
    [switch]$CreateMissing,
    [switch]$EmitJson
)

$directories = @(
    "docs/functional analysis",
    "docs/wireframes",
    "docs/technical",
    "docs/diagrams",
    "docs/reports",
    "frontend-tests"
)

$results = foreach ($dir in $directories) {
    $fullPath = Join-Path $Root $dir
    $exists = Test-Path -Path $fullPath -PathType Container

    if (-not $exists -and $CreateMissing) {
        New-Item -ItemType Directory -Force -Path $fullPath | Out-Null
        $exists = $true
    }

    [PSCustomObject]@{
        path = $dir
        exists = $exists
    }
}

if ($EmitJson) {
    $results | ConvertTo-Json -Depth 3
    exit 0
}

foreach ($result in $results) {
    if ($result.exists) {
        Write-Host "Directory verified: $($result.path)"
    } else {
        Write-Host "Directory missing: $($result.path)"
    }
}

$missingCount = ($results | Where-Object { -not $_.exists }).Count

if ($missingCount -eq 0) {
    Write-Host "All default SDLC directories are present."
} elseif ($CreateMissing) {
    Write-Host "Provisioned missing default SDLC directories."
} else {
    Write-Host "Some default SDLC directories are missing. Re-run with -CreateMissing to provision them."
}
