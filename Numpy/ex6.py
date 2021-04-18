import numpy as np
a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test element-wise for positive or negative infinity:")
print(np.isinf(a))
