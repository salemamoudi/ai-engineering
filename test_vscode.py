"""
Test VS Code Setup
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_setup():
    """Test if everything works"""
    print("✅ Python is working!")
    print(f"NumPy: {np.__version__}")
    print(f"Pandas: {pd.__version__}")
    
    # Test simple data
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    print("\nDataFrame:")
    print(data)
    
    return "✅ All tests passed!"

if __name__ == "__main__":
    result = test_setup()
    print(result)
