import pandas as pd
import numpy as np
num_series = pd.Series(np.take(list('0123456789'), np.random.randint(10, size=40)))
print("Original Series:")
print(num_series)
print("Frequency of each unique value of the said series.")
result = num_series.value_counts()
print(result)
