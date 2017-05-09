
# coding: utf-8

# In[4]:

import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
recent_grads = pd.read_csv("recent-grads.csv")
recent_grads.iloc[0]


# In[5]:

recent_grads.head()


# In[6]:

recent_grads.tail()


# In[7]:

recent_grads.describe()


# In[14]:

#Checking number of rows
raw_data_count = recent_grads.shape[0]


# In[17]:

#Dropping rows with missing values and comparing with old dataset
recent_grads = recent_grads.dropna()
cleaned_data_count = recent_grads.shape[0]
raw_data_count - cleaned_data_count


# In[19]:

#Generating a scatter plot of Sample Size vs Median
recent_grads.plot(x = "Sample_size", y = "Median", kind = "scatter", title = "Sample Size vs Median Income", figsize = (10,10))


# In[20]:

#Generating a scatter plot of Sample Size vs Unemployment Rate
recent_grads.plot(x = "Sample_size", y = "Unemployment_rate", kind = "scatter", title = "Sample Size vs Unemployment Rate", figsize = (10,10))


# In[21]:

#Generating a scatter plot of Full Time Employment vs Median Income
recent_grads.plot(x = "Full_time", y = "Median", kind = "scatter", title = "Full Time Employment vs Median Income", figsize = (10,10))


# In[22]:

#Generating a scatter plot of Women % vs Unemployment Rate
recent_grads.plot(x = "ShareWomen", y = "Unemployment_rate", kind = "scatter", title = "Women % vs Unemployment Rate", figsize = (10,10))


# In[23]:

#Generating a scatter plot of Male Graduates vs Median Income
recent_grads.plot(x = "Men", y = "Median", kind = "scatter", title = "Male Graduates vs Median Income", figsize = (10,10))


# In[24]:

#Generating a scatter plot of Female Graduates vs Median Income
recent_grads.plot(x = "Women", y = "Median", kind = "scatter", title = "Female Graduates vs Median Income", figsize = (10,10))


# In[38]:

#Generating histograms of the distributions of Sample Size, Median Income, Number Employed, Number of Full Time Graduates, % of Women, Unmployment Rate, # of Men and # of Women
fig = plt.figure(figsize=(10,48))
col_names = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]
for i in range(8):
    ax = fig.add_subplot(8, 1, i+1)
    ax = recent_grads[col_names[i]].plot(kind = "hist", rot = 45, title = col_names[i])


# In[47]:

import pandas.tools.plotting


# In[48]:

#Generating Scatter Matrix Plots for Sample Size vs Median and Sample Size vs Median vs Unemployment Rate
scatter_matrix(recent_grads[["Sample_size", "Median"]],figsize = (8,8))


# In[49]:

scatter_matrix(recent_grads[["Sample_size", "Median", "Unemployment_rate"]],figsize = (12,12))


# In[54]:

recent_grads[:10].plot.bar(x = "Major", y = "ShareWomen", legend = False)
recent_grads[len(recent_grads["Major"])-10:].plot.bar(x = "Major", y = "ShareWomen", legend = False)


# In[56]:

recent_grads[:10].plot.bar(x = "Major", y = "Unemployment_rate", legend = False)
recent_grads[len(recent_grads["Major"])-10:].plot.bar(x = "Major", y = "Unemployment_rate", legend = False)


# In[ ]:



