
# coding: utf-8

# In[25]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
get_ipython().magic('matplotlib inline')
movies = pd.read_csv("fandango_score_comparison.csv")
movies


# In[26]:

plt.hist(movies["Metacritic_norm_round"], range = (0,5))


# In[27]:

plt.hist(movies["Fandango_Stars"], range = (0,5))


# # Fandango vs Metacritic Scores
# The Metacritic scores seem to have a more even distribution centered around the 3.5 rating while the Fandango scores have almost all the values between the 3 and 5 range where the majority of the scores are skewed towards the 5 rating

# In[28]:

fd_mean = movies["Fandango_Stars"].mean()
fd_median = movies["Fandango_Stars"].median()
fd_stdev = movies["Fandango_Stars"].std()
mt_mean = movies["Metacritic_norm_round"].mean()
mt_median = movies["Metacritic_norm_round"].median()
mt_stdev = movies["Metacritic_norm_round"].std()
print(fd_mean, fd_median, fd_stdev)
print(mt_mean, mt_median, mt_stdev)


# In[29]:

plt.scatter(movies["Fandango_Stars"],movies["Metacritic_norm_round"])


# In[30]:

movies["fm_diff"] = np.abs(movies["Fandango_Stars"] - movies["Metacritic_norm_round"])
movies.sort_values(by = ["fm_diff"], ascending=False).head(5)


# In[33]:

r, p_value = stats.pearsonr(movies["Fandango_Stars"], movies["Metacritic_norm_round"])
r


# In[37]:

slope, intercept, rvalue, pvalue, stderr = stats.linregress(movies["Metacritic_norm_round"], movies["Fandango_Stars"])
pred_3 = 3 * slope + intercept
pred_3


# In[40]:

pred_1 = 1 * slope + intercept
pred_5 = 5 * slope + intercept
plt.scatter(movies["Metacritic_norm_round"], movies["Fandango_Stars"])
plt.plot([1.0,5.0],[pred_1,pred_5])
plt.xlim(1,5)
plt.show()


# In[ ]:



