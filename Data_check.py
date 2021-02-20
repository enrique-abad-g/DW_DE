

import numpy as np
import pandas as pd



data_1 = pd.read_csv('2021-02-06-03-04-06-CET-Historical-Report-GUSFacebook-2020-11-06--2021-02-06.csv')
data_2 = pd.read_csv('2021-02-07-03-02-27-CET-Historical-Report-GUSFacebook-2020-11-07--2021-02-07.csv')
data_3 = pd.read_csv('2021-02-08-03-02-18-CET-Historical-Report-GUSFacebook-2020-11-08--2021-02-08.csv')

# Check dates

print(data_1.Created.dtype)
print(data_1['Video Length'].dtype)

# They are not dates!

data_1.Created = pd.to_datetime(data_1.Created,format='%Y-%m-%d %H:%M:%S %Z')
data_2.Created = pd.to_datetime(data_2.Created,format='%Y-%m-%d %H:%M:%S %Z')
data_3.Created = pd.to_datetime(data_3.Created,format='%Y-%m-%d %H:%M:%S %Z')
data_1['Video Length'] = pd.to_timedelta(data_1['Video Length'])
data_2['Video Length'] = pd.to_timedelta(data_2['Video Length'])
data_3['Video Length'] = pd.to_timedelta(data_3['Video Length'])

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

# If we put everything together, are repeated URLs?

data_total = pd.concat([data_1,data_2,data_3])
print(len(data_total.URL.unique()),len(data_total.URL))

# Yes!


# Let's check if data from different days is different

data_total = pd.concat([data_1,data_2,data_3])

# If the standard deviation of the likes is not zero, that means that the amount
# of likes change for the same URL.
# (Everyday we get an updated number of likes of the post)

std_likes = data_total.groupby('URL')['Likes'].std()

print(std_likes[std_likes != 0])

# Let's see a couple of urls:
url_to_check1 = std_likes[std_likes != 0].index[0]
url_to_check2 = std_likes[std_likes != 0].index[1]

checkup_1 = data_total[data_total.URL == url_to_check1]
print(checkup_1['Likes'])
checkup_2 = data_total[data_total.URL == url_to_check2]
print(checkup_2['Likes'])

# Normalize the data

# 1NF
# It has to be. The data come from a csv file, and there would be some kind of
# error if a column has several values separated by commas

# 2NF
# It is. URL on itself is a primary key.

# 3NF
# "Page Name" and "User Name" depend on "Facebook Id" therefore, we can separate
# the table in two tables

# Table 1
data_userid = data_total[['Page Name','User Name','Facebook Id']]
data_userid = data_userid.drop_duplicates()
print(data_userid)

# Table 2 (FacebookID is the primary key in data_userid and the foering one in
# data_url)

data_url = data_total.drop(labels=['Page Name','User Name'],axis=1)
print(data_url)


# It may be that the overperforming score is dependent on the primary
# key through the likes, shares, etc, but I am not 100 % sure
# I should check it if there is time
