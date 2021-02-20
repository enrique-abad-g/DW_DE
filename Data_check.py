

import numpy as np
import pandas as pd



data_1 = pd.read_csv('2021-02-06-03-04-06-CET-Historical-Report-GUSFacebook-2020-11-06--2021-02-06.csv')
data_2 = pd.read_csv('2021-02-07-03-02-27-CET-Historical-Report-GUSFacebook-2020-11-07--2021-02-07.csv')
data_3 = pd.read_csv('2021-02-08-03-02-18-CET-Historical-Report-GUSFacebook-2020-11-08--2021-02-08.csv')

# Check dates

print(data_1.Created.dtype)

# Is not a date!

data_1.Created = pd.to_datetime(data_1.Created,format='%Y-%m-%d %H:%M:%S %Z')
data_2.Created = pd.to_datetime(data_2.Created,format='%Y-%m-%d %H:%M:%S %Z')
data_3.Created = pd.to_datetime(data_3.Created,format='%Y-%m-%d %H:%M:%S %Z')

# Do dates overlap?

print(data_1.Created.min(),data_1.Created.max())
print(data_2.Created.min(),data_2.Created.max())
print(data_3.Created.min(),data_3.Created.max())

# Yes!

# Is URL a primary key?

print(len(data_1.URL.unique()),len(data_1.URL))
print(len(data_2.URL.unique()),len(data_2.URL))
print(len(data_3.URL.unique()),len(data_3.URL))

# Yes!
