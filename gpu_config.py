"""GPU Configuration for AI Engineering Projects"""

import torch
import os

def setup_gpu():
    """Configure GPU settings for training"""
    
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print(f"GPU: {torch.cuda.get_device_name(0)}")
        print(f"CUDA Version: {torch.version.cuda}")
        torch.cuda.empty_cache()
        print("✅ GPU configured successfully")
        return device
    else:
        print("⚠️ No GPU detected, using CPU")
        return torch.device("cpu")

def get_device():
    """Return the best available device"""
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")

if __name__ == "__main__":
    device = setup_gpu()
    print(f"Device: {device}")
