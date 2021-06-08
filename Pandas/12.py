import pandas as pd
s = pd.Series(data = [1,2,3,4,5], index = ['A', 'B', 'C','D','E'])
print("Original Data Series:")
print(s)
s = s.reindex(index = ['B','A','C','D','E'])
print("Data Series after changing the order of index:")
print(s)
