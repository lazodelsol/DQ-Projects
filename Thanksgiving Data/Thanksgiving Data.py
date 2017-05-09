
# coding: utf-8

# In[1]:

import pandas as pd
data = pd.read_csv("thanksgiving.csv", encoding ="Latin-1")
print(data[0:5])


# In[2]:

data.columns


# In[3]:

data["Do you celebrate Thanksgiving?"].value_counts()


# In[4]:

data = data[data["Do you celebrate Thanksgiving?"] == "Yes"]
data


# In[5]:

data["What is typically the main dish at your Thanksgiving dinner?"].value_counts()


# In[10]:

data_tofurkey = data[data["What is typically the main dish at your Thanksgiving dinner?"] == "Tofurkey"]
data_tofurkey["Do you typically have gravy?"]


# In[12]:

apple_isnull = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"].isnull()
apple_isnull


# In[13]:

pumpkin_isnull = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"].isnull()
pumpkin_isnull


# In[14]:

pecan_isnull = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"].isnull()
pecan_isnull


# In[17]:

ate_pies = apple_isnull & pumpkin_isnull & pecan_isnull
ate_pies.value_counts()


# In[22]:

import re
def age_convert(age):
    if pd.isnull(age):
        return None
    else:
        split_age = age.split(" ")
        age_first = split_age[0]
        age_fixed = age_first.replace("+", "")
        age_int = int(age_fixed)
        return age_int
data["int_age"] = data["Age"].apply(age_convert)
data["int_age"]


# In[23]:

data["int_age"].describe()


# In[26]:

def money_convert(money):
    if pd.isnull(money):
        return None
    else:
        split_money = money.split(" ")
        money_first = split_money[0]
        if money_first == "Prefer":
            return None
        else:
            money1 = money_first.replace("$", "")
            money_fixed = money1.replace(",", "")
            money_int = int(money_fixed)
            return money_int
data["int_income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(money_convert)
data["int_income"]


# In[27]:

data["int_income"].describe()


# For both of these types of calculations, because we only chose the first number from the range given, the actual values are naturally skewed downwards. A better choice for either of these would be to take the average of the two values for each choice and used that in our calculations.

# In[30]:

under_150000 = data[data["int_income"] < 150000]
under_150000["How far will you travel for Thanksgiving?"].value_counts()


# In[33]:

over_150000 = data[data["int_income"] > 150000]
over_150000["How far will you travel for Thanksgiving?"].value_counts()


# These results are hard to compare given the vast difference in numbers. It would be better to do a normalized comparison between the two sets.

# In[44]:

data.pivot_table(
    index = "Have you ever tried to meet up with hometown friends on Thanksgiving night?",
    values = "int_age",
    columns = 'Have you ever attended a "Friendsgiving?"'
)


# In[46]:

data.pivot_table(
    index = "Have you ever tried to meet up with hometown friends on Thanksgiving night?",
    columns = 'Have you ever attended a "Friendsgiving?"',
    values = "int_income"
)


# In[ ]:



