"""Showcase various NumPy operations: indexing, slicing, flattening, appending, concatenation."""
import numpy as np

arr = np.arange(1, 13).reshape(3, 4)
print("Original array:\n", arr)

# Indexing
print("Element at (1,2):", arr[1, 2])

# Slicing
print("First two rows:\n", arr[:2, :])

# Flattening
flat = arr.flatten()
print("Flattened:", flat)

# Appending a row
appended = np.append(arr, [[13, 14, 15, 16]], axis=0)
print("Appended row:\n", appended)

# Concatenation (column‑wise)
extra_col = np.arange(100, 103).reshape(3, 1)
concat = np.concatenate((arr, extra_col), axis=1)
print("Concatenated column:\n", concat)