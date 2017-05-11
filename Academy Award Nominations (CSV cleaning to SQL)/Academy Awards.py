
# coding: utf-8

# In[148]:

import pandas as pd
data = pd.read_csv("academy_awards.csv", encoding = "ISO-8859-1")
data.head(5)


# In[149]:

data.iloc[:,3].value_counts()


# In[150]:

data["Year"] = data["Year"].str[0:4].astype(int)


# In[151]:

later_than_2000 = data[(data["Year"] > 2000)]
award_categories = ["Actor -- Leading Role", "Actor -- Supporting Role", "Actress -- Leading Role", "Actress -- Supporting Role"]
nominations = later_than_2000[later_than_2000["Category"].isin(award_categories)]
nominations


# In[152]:

mapping_dict = { 
    "NO": 0,
    "YES": 1
}
nominations["Won?"] = nominations["Won?"].map(mapping_dict)
nominations["Won"] = nominations["Won?"]


# In[153]:

col_names = ["Won?", "Unnamed: 5", "Unnamed: 6", "Unnamed: 7", "Unnamed: 8", "Unnamed: 9", "Unnamed: 10"]
final_nominations = data.drop(col_names, axis = 1)
final_nominations.head(5)


# In[154]:

additional_info_one = data["Additional Info"].str.rstrip("'}")
additional_info_two = additional_info_one.str.split(" {'")
movie_names = additional_info_two.str[0]
characters = additional_info_two.str[1]
final_nominations["Movie"] = movie_names
final_nominations["Character"] = characters
final_nominations = final_nominations.drop(["Additional Info"], axis = 1)


# In[155]:

final_nominations.head(5)


# In[156]:

import sqlite3
conn = sqlite3.connect("nominations.db")
final_nominations.to_sql("nominations", conn, index=False)
query_one = "pragma table_info(nominations);"
query_two = "select * from nominations limit 10;"
print(conn.execute(query_one).fetchall())
print(conn.execute(query_two).fetchall())
conn.close()


# In[ ]:



