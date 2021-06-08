import pandas as pd
series1 = pd.Series([1, 3, 5, 8, 10, 11, 15])
print("Original Series:")
print(series1)
print("\nDifference of differences between consecutive numbers of the said series:")
print(series1.diff().tolist())
print(series1.diff().diff().tolist())
