#!/usr/bin/env python3
"""
Walmart Black Friday Analysis App Launcher
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = [
        'streamlit', 'pandas', 'numpy', 'plotly', 
        'seaborn', 'matplotlib', 'scipy'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n📦 Install missing packages with:")
        print("   pip install -r requirements.txt")
        return False
    
    print("✅ All required packages are installed!")
    return True

def check_dataset():
    """Check if the dataset exists"""
    dataset_path = "Dataset/Walmart_data.csv"
    
    if os.path.exists(dataset_path):
        print(f"✅ Dataset found: {dataset_path}")
        return True
    else:
        print("❌ Dataset not found!")
        print("📁 Expected location: Dataset/Walmart_data.csv")
        print("\n💡 You can:")
        print("   1. Place your Walmart_data.csv file in the Dataset/ folder")
        print("   2. Run 'python sample_data.py' to generate sample data")
        return False

def main():
    """Main launcher function"""
    print("🛒 Walmart Black Friday Analysis App")
    print("=" * 50)
    
    # Check dependencies
    print("\n🔍 Checking dependencies...")
    if not check_dependencies():
        return
    
    # Check dataset
    print("\n📊 Checking dataset...")
    if not check_dataset():
        print("\n❌ Cannot start app without dataset!")
        return
    
    # Launch Streamlit app
    print("\n🚀 Starting Streamlit app...")
    print("🌐 The app will open in your default web browser")
    print("📱 If it doesn't open automatically, go to: http://localhost:8501")
    print("\n" + "=" * 50)
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"], check=True)
    except KeyboardInterrupt:
        print("\n👋 App stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error starting app: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    main() 