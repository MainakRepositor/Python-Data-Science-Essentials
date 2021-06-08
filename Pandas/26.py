import pandas as pd
from dateutil.parser import parse
date_series = pd.Series(['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019'])
print("Original Series:")
print(date_series)
print("\nNew dates:")
result = date_series.map(lambda d: parse('11 ' + d))
print(result)
