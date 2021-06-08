import pandas as pd
result = pd.Series(pd.date_range('2020-01-01', periods=52, freq='W-SUN'))
print("All Sundays of 2019:")
print(result)
