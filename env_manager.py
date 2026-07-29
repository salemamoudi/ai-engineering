#!/usr/bin/env python3
"""Environment Management Script"""

import os
import sys
import subprocess

def get_env_info():
    """Get info about current environment"""
    info = {
        "python": sys.version.split()[0],
        "venv": os.environ.get('VIRTUAL_ENV', 'Not in virtual environment'),
        "packages": []
    }
    
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'list', '--format=freeze'],
            capture_output=True, text=True
        )
        info["packages"] = result.stdout.split('\n')[:5]
    except:
        pass
    
    return info

def check_environment():
    """Check current environment status"""
    info = get_env_info()
    print("=" * 50)
    print("Environment Information")
    print("=" * 50)
    print(f"Python: {info['python']}")
    print(f"Virtual Env: {info['venv']}")
    print(f"\nPackages (first 5):")
    for pkg in info['packages']:
        if pkg:
            print(f"  - {pkg}")
    print("=" * 50)

if __name__ == "__main__":
    check_environment()
