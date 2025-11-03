#!/bin/bash
# PythonAnywhere deployment script
# Save this in your PythonAnywhere files and run it after pushing to GitHub

echo "========================================="
echo "  Updating Tatana Blog from GitHub"
echo "========================================="

# Navigate to project directory
cd /home/ttatana/ttatana-blog

echo "📥 Pulling latest changes from GitHub..."
git pull origin main

echo "📦 Collecting static files..."
python3.13 manage.py collectstatic --noinput

echo "🔄 Running migrations (if any)..."
python3.13 manage.py migrate

echo "✅ Deployment complete!"
echo "🌐 Your blog is updated at: https://ttatana.pythonanywhere.com/"
echo ""
echo "⚠️  Don't forget to click 'Reload' in the Web tab!"