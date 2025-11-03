#!/usr/bin/env python3
"""
Tatana Blog Deployment Script
Automates the process of deploying changes to PythonAnywhere
"""

import subprocess
import sys
from datetime import datetime

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}:")
        print(f"   {e.stderr}")
        return False

def main():
    print("=" * 50)
    print("   🚀 Tatana Blog Deployment Script")
    print("=" * 50)
    
    # Get commit message
    commit_msg = input("\n📝 Enter commit message (or press Enter for default): ").strip()
    if not commit_msg:
        commit_msg = f"Update blog - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    
    # Step 1: Add changes
    if not run_command("git add .", "Adding changes to Git"):
        return
    
    # Step 2: Commit changes
    if not run_command(f'git commit -m "{commit_msg}"', "Committing changes"):
        print("ℹ️  No changes to commit or commit failed")
    
    # Step 3: Push to GitHub
    if not run_command("git push origin main", "Pushing to GitHub"):
        return
    
    print("\n" + "=" * 50)
    print("✅ LOCAL DEPLOYMENT COMPLETE!")
    print("=" * 50)
    
    print("\n📋 NEXT STEPS FOR PYTHONANYWHERE:")
    print("1. Go to PythonAnywhere Bash Console")
    print("2. Run: cd /home/ttatana/ttatana-blog")
    print("3. Run: git pull origin main")
    print("4. Run: python3.13 manage.py collectstatic --noinput")
    print("5. Click 'Reload' in Web tab")
    
    print(f"\n🌐 Your blog: https://ttatana.pythonanywhere.com/")
    print("\n🎉 Deployment ready!")

if __name__ == "__main__":
    main()