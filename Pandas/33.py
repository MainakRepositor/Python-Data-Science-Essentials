import numpy as np
import pandas as pd
char_list = list('ABCDEFGHIJKLMNOP')
num_arra = np.arange(8)
num_dict = dict(zip(char_list, num_arra))
num_ser = pd.Series(num_dict)
df = num_ser.to_frame().reset_index()
print(df.head())
