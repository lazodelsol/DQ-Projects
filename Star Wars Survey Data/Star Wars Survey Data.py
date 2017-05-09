
# coding: utf-8

# In[87]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
get_ipython().magic('matplotlib inline')

star_wars = pd.read_csv("star_wars.csv", encoding = "ISO-8859-1")
star_wars.shape


# In[88]:

star_wars = star_wars[star_wars["RespondentID"].notnull()]
star_wars.shape


# In[89]:

star_wars.head(3)


# In[90]:

to_boolean = {
    "Yes" : True,
    "No" : False
}
cols = ["Have you seen any of the 6 films in the Star Wars franchise?", "Do you consider yourself to be a fan of the Star Wars film franchise?"]
for col in cols:
    star_wars[col] = star_wars[col].map(to_boolean)
star_wars[cols]


# # Creating mapping dictionary & renaming columns

# In[91]:

movie_titles = star_wars.columns[3:9]
movie_mapping = {
    "Star Wars: Episode I  The Phantom Menace": True,
    np.nan: False,
    "Star Wars: Episode II  Attack of the Clones": True,
    "Star Wars: Episode III  Revenge of the Sith": True,
    "Star Wars: Episode IV  A New Hope": True,
    "Star Wars: Episode V The Empire Strikes Back": True,
    "Star Wars: Episode VI Return of the Jedi": True
}

for col in star_wars.columns[3:9]:
    star_wars[col] = star_wars[col].map(movie_mapping)
star_wars.head(5)


# In[92]:

newnames = ["seen_1", "seen_2", "seen_3", "seen_4", "seen_5", "seen_6"]
title_map = {}
for i in range(1,7):
    title_map[movie_titles[i-1]] = newnames[i-1]
title_map
star_wars.rename(columns = title_map, inplace = True)
star_wars.head(5)


# In[102]:

star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)
rankingnames = ["ranking_1", "ranking_2", "ranking_3", "ranking_4", "ranking_5", "ranking_6"]
ranking_map = {}
for i in range(6):
    ranking_map[star_wars.columns[i+9]] = rankingnames[i]
ranking_map
star_wars.rename(columns = ranking_map, inplace = True)
star_wars.head(5)


# In[107]:

mean_rankings = star_wars[star_wars.columns[9:15]].mean()
mean_rankings.plot.bar()


# In[108]:

seen_sum = star_wars[star_wars.columns[3:9]].sum()
seen_sum.plot.bar()


# # Finding mean/total seen for male/females separately

# In[110]:

males = star_wars[star_wars["Gender"] == "Male"]
females = star_wars[star_wars["Gender"] == "Female"]
#For Males
mean_rankings = males[males.columns[9:15]].mean()
mean_rankings.plot.bar()


# In[111]:

seen_sum = males[males.columns[3:9]].sum()
seen_sum.plot.bar()


# In[112]:

#For females
mean_rankings = females[females.columns[9:15]].mean()
mean_rankings.plot.bar()


# In[113]:

seen_sum = females[females.columns[3:9]].sum()
seen_sum.plot.bar()


# In[ ]:



