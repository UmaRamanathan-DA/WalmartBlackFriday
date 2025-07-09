#!/usr/bin/env python3
"""
Deployment Helper Script for Walmart Black Friday Analysis
"""

import subprocess
import sys
import os
import webbrowser
from pathlib import Path

def check_git_status():
    """Check if git repository is properly configured"""
    try:
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Git repository found")
            return True
        else:
            print("❌ Git repository not found or not initialized")
            return False
    except FileNotFoundError:
        print("❌ Git not installed. Please install Git first.")
        return False

def check_files():
    """Check if all required files exist"""
    required_files = [
        'app.py',
        'requirements.txt',
        'README.md',
        'Dataset/Walmart_data.csv'
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("✅ All required files found")
    return True

def commit_and_push():
    """Commit and push changes to GitHub"""
    try:
        # Add all files
        subprocess.run(['git', 'add', '.'], check=True)
        print("✅ Files added to git")
        
        # Commit
        subprocess.run(['git', 'commit', '-m', 'Update app for deployment'], check=True)
        print("✅ Changes committed")
        
        # Push
        subprocess.run(['git', 'push'], check=True)
        print("✅ Changes pushed to GitHub")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Git operation failed: {e}")
        return False

def open_streamlit_cloud():
    """Open Streamlit Cloud in browser"""
    url = "https://share.streamlit.io"
    print(f"🌐 Opening Streamlit Cloud: {url}")
    webbrowser.open(url)

def main():
    """Main deployment function"""
    print("🚀 Walmart Black Friday Analysis - Deployment Helper")
    print("=" * 60)
    
    # Check prerequisites
    print("\n🔍 Checking prerequisites...")
    if not check_git_status():
        print("\n❌ Please initialize git repository first:")
        print("   git init")
        print("   git remote add origin https://github.com/your-username/WalmartBlackFriday.git")
        return
    
    if not check_files():
        print("\n❌ Please ensure all required files are present")
        return
    
    # Deploy options
    print("\n🌐 Deployment Options:")
    print("1. Streamlit Cloud (Recommended - FREE)")
    print("2. Railway (FREE)")
    print("3. Render (FREE)")
    print("4. Heroku (Paid)")
    
    choice = input("\nSelect deployment option (1-4): ").strip()
    
    if choice == "1":
        print("\n🚀 Deploying to Streamlit Cloud...")
        if commit_and_push():
            print("\n✅ Code pushed to GitHub!")
            print("\n📋 Next steps:")
            print("1. Go to https://share.streamlit.io")
            print("2. Sign in with your GitHub account")
            print("3. Click 'New app'")
            print("4. Select your repository: WalmartBlackFriday")
            print("5. Set path to: app.py")
            print("6. Click 'Deploy'")
            
            open_browser = input("\nOpen Streamlit Cloud in browser? (y/n): ").lower()
            if open_browser == 'y':
                open_streamlit_cloud()
    
    elif choice == "2":
        print("\n🚀 Deploying to Railway...")
        if commit_and_push():
            print("\n✅ Code pushed to GitHub!")
            print("\n📋 Next steps:")
            print("1. Go to https://railway.app")
            print("2. Sign in with your GitHub account")
            print("3. Click 'New Project'")
            print("4. Select 'Deploy from GitHub repo'")
            print("5. Select your WalmartBlackFriday repository")
            print("6. Railway will automatically detect and deploy")
    
    elif choice == "3":
        print("\n🚀 Deploying to Render...")
        if commit_and_push():
            print("\n✅ Code pushed to GitHub!")
            print("\n📋 Next steps:")
            print("1. Go to https://render.com")
            print("2. Sign in with your GitHub account")
            print("3. Click 'New Web Service'")
            print("4. Connect your WalmartBlackFriday repository")
            print("5. Configure:")
            print("   - Build Command: pip install -r requirements.txt")
            print("   - Start Command: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0")
            print("6. Click 'Create Web Service'")
    
    elif choice == "4":
        print("\n🚀 Deploying to Heroku...")
        print("\n📋 Prerequisites:")
        print("1. Install Heroku CLI")
        print("2. Run: heroku login")
        print("3. Run: heroku create your-app-name")
        print("4. Run: git push heroku main")
        print("5. Run: heroku open")
    
    else:
        print("❌ Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main() 