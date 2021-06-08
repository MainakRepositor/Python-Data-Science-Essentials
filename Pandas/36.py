import pandas as pd
nums = pd.Series([1, 3, 7, 12, 88, 23, 3, 1, 9, 0])
print("Original Series:")
print(nums)
print("Index of the first occurrence of the smallest and largest value of the said series:")
print(nums.idxmin())
print(nums.idxmax())
