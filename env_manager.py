#!/usr/bin/env python3
"""
Environment Management Script
Helps manage Python virtual environments
"""

import os
import sys
import subprocess
import platform

def get_env_info():
    """Get information about the current environment"""
    info = {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "venv": os.environ.get('VIRTUAL_ENV', 'Not in a virtual environment'),
        "packages": []
    }
    
    # Get installed packages
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'list', '--format=freeze'],
            capture_output=True, text=True
        )
        info["packages"] = result.stdout.split('\n')[:5]  # Show first 5
    except:
        pass
    
    return info

def create_environment(name=".venv"):
    """Create a new virtual environment"""
    print(f"Creating environment: {name}")
    subprocess.run([sys.executable, '-m', 'venv', name])
    print(f"✅ Environment created: {name}")
    print(f"Activate with: source {name}/bin/activate")

def check_environment():
    """Check current environment status"""
    info = get_env_info()
    print("=" * 50)
    print("Environment Information")
    print("=" * 50)
    print(f"Python: {info['python']}")
    print(f"Platform: {info['platform']}")
    print(f"Virtual Env: {info['venv']}")
    print(f"\nPackages (first 5):")
    for pkg in info['packages']:
        if pkg:
            print(f"  - {pkg}")
    print("=" * 50)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "create":
            create_environment(sys.argv[2] if len(sys.argv) > 2 else ".venv")
        elif sys.argv[1] == "info":
            check_environment()
        else:
            print("Usage: python env_manager.py [create|info]")
    else:
        check_environment()
