import pandas as pd
num_series = pd.Series(list('2390238923902390239023'))
element_pos = [0, 2, 6, 11, 21]
print("Original Series:")
print(num_series)
result = num_series.take(element_pos)
print("\nExtract items at given positions of the said series:")
print(result)
