import pandas as pd
nums1 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
nums2 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print("Original Series:")
print(nums1)
print(nums2)
print("Check 2 series are equal or not?")
print(nums1 == nums2)

