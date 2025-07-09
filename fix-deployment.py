#!/usr/bin/env python3
"""
Deployment Fix Script for Walmart Black Friday Analysis
"""

import os
import shutil
from pathlib import Path

def fix_requirements():
    """Fix requirements.txt with stable versions"""
    print("🔧 Fixing requirements.txt...")
    
    # Backup current requirements
    if Path("requirements.txt").exists():
        shutil.copy("requirements.txt", "requirements.txt.backup")
        print("✅ Backed up current requirements.txt")
    
    # Use stable requirements
    if Path("requirements-stable.txt").exists():
        shutil.copy("requirements-stable.txt", "requirements.txt")
        print("✅ Updated requirements.txt with stable versions")
    else:
        print("❌ requirements-stable.txt not found")
        return False
    
    return True

def check_files():
    """Check if all required files exist"""
    required_files = [
        'app.py',
        'requirements.txt',
        'runtime.txt',
        'Procfile',
        '.streamlit/config.toml'
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

def create_runtime_txt():
    """Create runtime.txt if it doesn't exist"""
    if not Path("runtime.txt").exists():
        print("📝 Creating runtime.txt...")
        with open("runtime.txt", "w") as f:
            f.write("python-3.11\n")
        print("✅ Created runtime.txt")
    else:
        print("✅ runtime.txt already exists")

def main():
    """Main fix function"""
    print("🔧 Walmart Black Friday Analysis - Deployment Fix")
    print("=" * 50)
    
    # Check files
    print("\n🔍 Checking files...")
    if not check_files():
        print("\n❌ Please ensure all required files are present")
        return
    
    # Fix requirements
    print("\n📦 Fixing requirements...")
    if fix_requirements():
        print("✅ Requirements fixed successfully")
    else:
        print("❌ Failed to fix requirements")
        return
    
    # Create runtime.txt
    print("\n🐍 Setting Python version...")
    create_runtime_txt()
    
    print("\n✅ Deployment fixes completed!")
    print("\n📋 Next steps:")
    print("1. Commit the changes:")
    print("   git add .")
    print("   git commit -m 'Fix deployment dependencies'")
    print("   git push origin main")
    print("\n2. Redeploy on Streamlit Cloud")
    print("3. The app should now deploy successfully")

if __name__ == "__main__":
    main() 