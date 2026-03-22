Describe "validate-project-structure.ps1" {
    BeforeAll {
        $ScriptPath = Join-Path $PSScriptRoot "..\scripts\validate-project-structure.ps1"
    }

    It "reports missing directories in JSON mode without creating them" {
        $root = Join-Path ([System.IO.Path]::GetTempPath()) ([System.Guid]::NewGuid().ToString())
        New-Item -ItemType Directory -Path $root | Out-Null

        try {
            $json = & $ScriptPath -Root $root -EmitJson
            $data = $json | ConvertFrom-Json

            $data.Count | Should Be 6
            ($data | Where-Object { $_.exists -eq $true }).Count | Should Be 0
            (Test-Path (Join-Path $root "docs")) | Should Be $false
        }
        finally {
            Remove-Item -Recurse -Force $root
        }
    }

    It "creates the default directories when -CreateMissing is supplied" {
        $root = Join-Path ([System.IO.Path]::GetTempPath()) ([System.Guid]::NewGuid().ToString())
        New-Item -ItemType Directory -Path $root | Out-Null

        try {
            & $ScriptPath -Root $root -CreateMissing | Out-Null

            Test-Path (Join-Path $root "docs/functional analysis") | Should Be $true
            Test-Path (Join-Path $root "docs/wireframes") | Should Be $true
            Test-Path (Join-Path $root "docs/technical") | Should Be $true
            Test-Path (Join-Path $root "docs/diagrams") | Should Be $true
            Test-Path (Join-Path $root "docs/reports") | Should Be $true
            Test-Path (Join-Path $root "frontend-tests") | Should Be $true
        }
        finally {
            Remove-Item -Recurse -Force $root
        }
    }
}
