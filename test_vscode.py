"""Test VS Code Setup"""

import sys
import numpy as np
import pandas as pd

print(f"Python: {sys.version[:50]}")
print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")

# Test DataFrame
data = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
print("\nDataFrame:")
print(data)

print("\n✅ VS Code is working!")
