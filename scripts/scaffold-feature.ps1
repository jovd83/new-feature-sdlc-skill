param (
    [Parameter(Mandatory = $true)]
    [string]$Title,

    [Parameter(Mandatory = $true)]
    [ValidateSet("Epic", "Technical", "Report")]
    [string]$Type,

    [string]$Id = "FEAT-XXX",
    [string]$Root = ".",
    [switch]$Force
)

function ConvertTo-KebabCase {
    param([string]$Value)

    $normalized = $Value.ToLower() -replace "[^a-z0-9]", "-" -replace "-+", "-"
    return $normalized.Trim("-")
}

function New-ScaffoldContent {
    param(
        [string]$DocumentType,
        [string]$DocumentTitle,
        [string]$TraceabilityId
    )

    switch ($DocumentType) {
        "Epic" {
            return @"
# Feature Plan: $DocumentTitle
Traceability ID: $TraceabilityId

## Problem Statement
- What user or business outcome is being pursued?

## Scope
- In scope:
- Out of scope:

## Acceptance Criteria
- Given ...
- When ...
- Then ...

## Risks and Dependencies
- Dependencies:
- Assumptions:
- Open questions:

## Linked Technical Artifacts
- Technical design:
- Wireframes or UX notes:
"@
        }
        "Technical" {
            return @"
# Technical Design: $DocumentTitle
Traceability ID: $TraceabilityId

## Context
- Existing components involved:
- Architectural constraints:

## Proposed Changes
- Application logic:
- Interfaces or contracts:
- Data or persistence:
- Rollout or migration:

## Validation Plan
- Automated tests:
- Manual verification:
- Coverage expectations:

## Dependency Notes
- New dependencies:
- Why they are justified:
"@
        }
        "Report" {
            return @"
### Feature: $DocumentTitle
Technical ID: $TraceabilityId

#### Scope Summary
- Requested outcome:
- Implemented scope:
- Explicit non-goals:

#### Planning and Traceability
- Approval source:
- Planning artifacts:
- Acceptance criteria or equivalent references:

#### Technical Design
- Architecture or technical docs updated:
- Diagrams updated:
- Key design decisions:

#### Implementation Highlights
- Main code changes:
- Key modules or files touched:
- Dependencies added or changed:

#### Verification
- Tests added or updated:
- Commands run:
- Coverage result:
- Manual verification:

#### Documentation and Operational Updates
- README or setup changes:
- User-facing docs:
- Release notes, changelog, or migration notes:

#### Risks and Follow-ups
- Open risks:
- Deferred work:
- Blockers or deviations:

#### Final Status
- Status:
- Ready for review:
- Ready for release:
"@
        }
    }
}

$kebabTitle = ConvertTo-KebabCase -Value $Title

switch ($Type) {
    "Epic" {
        $dir = Join-Path $Root "docs/functional analysis"
        $file = Join-Path $dir "feature-$kebabTitle.md"
    }
    "Technical" {
        $dir = Join-Path $Root "docs/technical"
        $file = Join-Path $dir "$kebabTitle.md"
    }
    "Report" {
        $dir = Join-Path $Root "docs/reports"
        $file = Join-Path $dir "$kebabTitle-report.md"
    }
}

if (-not (Test-Path -Path $dir -PathType Container)) {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
}

if ((Test-Path -Path $file -PathType Leaf) -and -not $Force) {
    Write-Host "File already exists: $file"
    Write-Host "Re-run with -Force to overwrite the scaffold."
    exit 0
}

$content = New-ScaffoldContent -DocumentType $Type -DocumentTitle $Title -TraceabilityId $Id
Set-Content -Path $file -Value $content

Write-Host "Scaffolded $Type document at: $file"
