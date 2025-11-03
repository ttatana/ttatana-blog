@echo off
echo ========================================
echo   Deploying Tatana Blog to Production
echo ========================================

echo.
echo [1/4] Adding changes to Git...
git add .

echo.
set /p commit_msg="Enter commit message (or press Enter for default): "
if "%commit_msg%"=="" set commit_msg=Update blog

echo [2/4] Committing changes...
git commit -m "%commit_msg%"

echo.
echo [3/4] Pushing to GitHub...
git push origin main

echo.
echo [4/4] Deployment complete!
echo.
echo Next steps:
echo 1. Go to PythonAnywhere Bash Console
echo 2. Run: cd /home/ttatana/ttatana-blog
echo 3. Run: git pull origin main
echo 4. Run: python3.13 manage.py collectstatic --noinput
echo 5. Click 'Reload' in Web tab
echo.
echo Your changes are now live at: https://ttatana.pythonanywhere.com/
echo.
pause