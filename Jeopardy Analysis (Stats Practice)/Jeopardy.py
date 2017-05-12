
# coding: utf-8

# In[78]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from scipy.stats import chisquare

get_ipython().magic('matplotlib inline')
jeopardy = pd.read_csv("jeopardy.csv")
jeopardy.head(5)


# In[79]:

jeopardy.columns
jeopardy.columns = jeopardy.columns.str.strip().str.replace(" ","")


# In[80]:

jeopardy.columns


# In[81]:

def normalize_text(string):
    string_lower = string.lower()
    string_punc_removed = re.sub("[^A-Za-z0-9\s]", "", string_lower)
    return string_punc_removed
jeopardy["clean_question"] = jeopardy["Question"].apply(normalize_text)
jeopardy["clean_answer"] = jeopardy["Answer"].apply(normalize_text)


# In[82]:

def normalize_value(string):
    string_punc_removed = re.sub("[^A-Za-z0-9\s]", "", string)
    try:
        string_int = int(string_punc_removed)
    except Exception:
        string_int = 0
    return string_int
jeopardy["clean_value"] = jeopardy["Value"].apply(normalize_value)


# In[83]:

jeopardy["AirDate"] = pd.to_datetime(jeopardy["AirDate"])


# # Finding out if the answer is in the question

# In[84]:

def match_count(row):
    match_count = 0
    split_answer = row["clean_answer"].split(" ")
    split_question = row["clean_question"].split(" ")
    if "the" in split_answer:
        split_answer.remove("the")
    if len(split_answer) == 0:
        return 0
    for answer in split_answer:
        if answer in split_question:
            match_count += 1
    return match_count / len(split_answer)

jeopardy["answer_in_question"] = jeopardy.apply(match_count, axis = 1)


# In[85]:

jeopardy["answer_in_question"].mean()


# In[86]:

question_overlap = []
terms_used = set()
for index, row in jeopardy.iterrows():
    split_question = row["clean_question"].split(" ")
    split_question = [q for q in split_question if len(q) > 5]
    match_count = 0
    for word in split_question:
        if word in terms_used:
            match_count += 1
        terms_used.add(word)
    if len(split_question) > 0:
        match_count = match_count / len(split_question)
    question_overlap.append(match_count)
jeopardy["question_overlap"] = question_overlap
jeopardy["question_overlap"].mean()


# In[87]:

def greater_than_800(row):
    if row["clean_value"] > 800:
        return 1
    else:
        return 0
jeopardy["high_value"] = jeopardy.apply(greater_than_800, axis = 1)


# In[88]:

def assign_count(string):
    low_count = 0
    high_count = 0
    for index, row in jeopardy.iterrows():
        split_question = row["clean_question"].split(" ")
        if string in split_question:
            if row["high_value"] == 1:
                high_count += 1
            else:
                low_count += 1
    return high_count, low_count
terms_used = list(terms_used)
comparison_terms = terms_used[:5]
observed_expected = []
for term in comparison_terms:
    observed_expected.append(assign_count(term))
    
observed_expected


# In[89]:

high_value_count = jeopardy[jeopardy["high_value"] == 1].shape[0]
low_value_count = jeopardy[jeopardy["high_value"] == 0].shape[0]

chi_squared = []
for value in observed_expected:
    total = sum(value)
    total_prop = total / jeopardy.shape[0]
    high_value_expected = total_prop * high_value_count
    low_value_expected = total_prop * low_value_count
    
    observed = np.array([obs[0], obs[1]])
    expected = np.array([high_value_expected, low_value_expected])
    chi_squared.append(chisquare(observed, expected))

