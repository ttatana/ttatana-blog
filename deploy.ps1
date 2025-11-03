# Tatana Blog Deployment Script
# PowerShell version for Windows users

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Deploying Tatana Blog to Production" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# Get commit message
$commitMsg = Read-Host "`nEnter commit message (or press Enter for default)"
if ([string]::IsNullOrWhiteSpace($commitMsg)) {
    $commitMsg = "Update blog - $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
}

Write-Host "`n[1/4] Adding changes to Git..." -ForegroundColor Yellow
git add .

Write-Host "`n[2/4] Committing changes..." -ForegroundColor Yellow
git commit -m $commitMsg

Write-Host "`n[3/4] Pushing to GitHub..." -ForegroundColor Yellow
git push origin main

Write-Host "`n[4/4] Deployment complete!" -ForegroundColor Green

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "   LOCAL DEPLOYMENT COMPLETE!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan

Write-Host "`nNext steps for PythonAnywhere:" -ForegroundColor Yellow
Write-Host "1. Go to PythonAnywhere Bash Console"
Write-Host "2. Run: cd /home/ttatana/ttatana-blog"
Write-Host "3. Run: git pull origin main"
Write-Host "4. Run: python3.13 manage.py collectstatic --noinput"
Write-Host "5. Click 'Reload' in Web tab"

Write-Host "`nYour blog: https://ttatana.pythonanywhere.com/" -ForegroundColor Cyan

Read-Host "`nPress Enter to exit"