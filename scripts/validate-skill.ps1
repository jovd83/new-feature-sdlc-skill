# Validate Skill Repository
# Runs high-level checks, eval generation, and Pester tests.

Write-Host "--- Running Quick Validator ---" -ForegroundColor Cyan
python .\scripts\quick_validate.py .
if ($LASTEXITCODE -ne 0) {
    Write-Host "Quick validation failed!" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host "`n--- Generating Eval View ---" -ForegroundColor Cyan
python .\scripts\generate_eval_view.py .
if ($LASTEXITCODE -ne 0) {
    Write-Host "Eval view generation failed!" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host "`n--- Running Pester Tests ---" -ForegroundColor Cyan
Invoke-Pester .\tests
if ($LASTEXITCODE -ne 0) {
    Write-Host "Pester tests failed!" -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host "`nValidation complete!" -ForegroundColor Green
