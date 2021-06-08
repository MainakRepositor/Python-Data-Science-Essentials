import pandas as pd
date_series = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
print("Original Series:")
print(date_series)
print("\nSeries of date strings to a timeseries:")
print(pd.to_datetime(date_series))
