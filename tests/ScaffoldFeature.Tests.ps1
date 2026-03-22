Describe "scaffold-feature.ps1" {
    BeforeAll {
        $ScriptPath = Join-Path $PSScriptRoot "..\scripts\scaffold-feature.ps1"
    }

    It "creates an Epic scaffold with the expected filename and sections" {
        $root = Join-Path ([System.IO.Path]::GetTempPath()) ([System.Guid]::NewGuid().ToString())
        New-Item -ItemType Directory -Path $root | Out-Null

        try {
            & $ScriptPath -Title "Forgot Password" -Type Epic -Id "FEAT-42" -Root $root | Out-Null
            $file = Join-Path $root "docs/functional analysis/feature-forgot-password.md"

            Test-Path $file | Should Be $true
            $content = Get-Content $file -Raw
            $content | Should Match "Feature Plan: Forgot Password"
            $content | Should Match "Traceability ID: FEAT-42"
            $content | Should Match "## Acceptance Criteria"
        }
        finally {
            Remove-Item -Recurse -Force $root
        }
    }

    It "creates a report scaffold in docs/reports" {
        $root = Join-Path ([System.IO.Path]::GetTempPath()) ([System.Guid]::NewGuid().ToString())
        New-Item -ItemType Directory -Path $root | Out-Null

        try {
            & $ScriptPath -Title "SSO Rollout" -Type Report -Id "FEAT-7" -Root $root | Out-Null
            $file = Join-Path $root "docs/reports/sso-rollout-report.md"

            Test-Path $file | Should Be $true
            $content = Get-Content $file -Raw
            $content | Should Match "### Feature: SSO Rollout"
            $content | Should Match "#### Verification"
            $content | Should Match "#### Final Status"
        }
        finally {
            Remove-Item -Recurse -Force $root
        }
    }

    It "does not overwrite an existing file unless -Force is supplied" {
        $root = Join-Path ([System.IO.Path]::GetTempPath()) ([System.Guid]::NewGuid().ToString())
        New-Item -ItemType Directory -Path $root | Out-Null

        try {
            & $ScriptPath -Title "Audit Log" -Type Technical -Id "FEAT-9" -Root $root | Out-Null
            $file = Join-Path $root "docs/technical/audit-log.md"
            Set-Content -Path $file -Value "custom"

            & $ScriptPath -Title "Audit Log" -Type Technical -Id "FEAT-9" -Root $root | Out-Null
            (Get-Content $file -Raw) | Should Be "custom`r`n"

            & $ScriptPath -Title "Audit Log" -Type Technical -Id "FEAT-9" -Root $root -Force | Out-Null
            (Get-Content $file -Raw) | Should Match "Technical Design: Audit Log"
        }
        finally {
            Remove-Item -Recurse -Force $root
        }
    }
}
