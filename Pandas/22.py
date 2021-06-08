import pandas as pd
series1 = pd.Series(['php', 'python', 'java', 'c#'])
print("Original Series:")
print(series1)
result = series1.map(lambda x: x[0].upper() + x[1:-1] + x[-1].upper())
print("\nFirst and last character of each word to upper case:")
print(result)
