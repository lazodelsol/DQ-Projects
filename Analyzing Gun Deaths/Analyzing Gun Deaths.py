
# coding: utf-8

# In[23]:

import csv
f = open("guns.csv", "r")
data = list(csv.reader(f))
print(data[0:5])


# In[24]:

headers = data[0]
data = data[1:len(data)]
print(headers)
print(data[0:5])


# In[25]:

years = [row[1] for row in data]
year_counts = {}
for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1
print(year_counts)


# In[26]:

import datetime
dates = [datetime.datetime(year = int(row[1]), month = int(row[2]), day = 1) for row in data]
print(dates[0:5])


# In[28]:

date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1
print(date_counts)


# In[29]:

date_counts


# In[30]:

sexes = [row[5] for row in data]
races = [row[7] for row in data]
sex_counts = {}
race_counts = {}
for race in races:
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1
for sex in sexes:
    if sex in sex_counts:
        sex_counts[sex] += 1
    else:
        sex_counts[sex] = 1
sex_counts


# In[31]:

race_counts


# In[32]:

census = list(csv.reader(open("census.csv","r")))
census


# In[15]:

mapping = {
    "Asian/Pacific Islander" : 15159516 + 674625,
    "Black": 40250635,
    "Native American/Native Alaskan": 3739506,
    "Hispanic": 44618105,
    "White": 197318956
}


# In[33]:

mapping


# In[34]:

race_per_hundredk = {}
for race in race_counts:
    race_per_hundredk[race] = race_counts[race] / mapping[race] * 10000
race_per_hundredk


# In[35]:

intents = [row[3] for row in data]
races = [row[7] for row in data]
intents


# In[36]:

races


# In[37]:

homocide_race_per_hundredk = {}
for i, race in enumerate(races):
    if intents[i] == "Homicide":
        if race in homocide_race_per_hundredk:
            homocide_race_per_hundredk[race] += 1
        else:
            homocide_race_per_hundredk[race] = 1
homocide_race_per_hundredk
    


# In[38]:

for race in homocide_race_per_hundredk:
    homocide_race_per_hundredk[race] = homocide_race_per_hundredk[race]/mapping[race] * 100000
homocide_race_per_hundredk


# In[ ]:



