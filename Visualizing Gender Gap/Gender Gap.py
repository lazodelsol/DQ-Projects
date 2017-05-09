
# coding: utf-8

# In[20]:

get_ipython().magic('matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)
cb_dark_gray = (171/255, 171/255, 171/255)
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']

fig = plt.figure(figsize=(18, 3))

for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    
    if sp == 0:
        ax.text(2005, 87, 'Men')
        ax.text(2002, 8, 'Women')
    elif sp == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2001, 35, 'Women')
plt.show()


# In[2]:

stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering', 'Computer Science']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']


# In[28]:

# Generates set of charts comparing the gender gap between 3 different subsets of majors. Additional cleaning has been done to the graphs as part of the exercise to facilitate comprehension

fig = plt.figure(figsize=(20,20))
# Generating the first column of graphs
for sp in range(0,6):
    col_index = (3 * sp) + 1
    ax = fig.add_subplot(6,3,col_index)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_yticks([0,100])
    ax.set_title(stem_cats[sp])
    ax.axhline(50, c=cb_dark_gray, alpha=0.3)
    if sp == 5:
        ax.tick_params(bottom="off", top="off", left="off", right="off")
    else:
        ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom="off")
    
    if sp == 0:
        ax.text(2005, 90, 'Women')
        ax.text(2007, 6, 'Men')
    elif sp == 5:
        ax.text(2007, 70, 'Men')
        ax.text(2005, 25, 'Women')
        
# Generating the second column of graphs
for sp in range(0,5):
    col_index = (3 * sp) + 2
    ax = fig.add_subplot(6,3,col_index)
    ax.plot(women_degrees['Year'], women_degrees[lib_arts_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[lib_arts_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_yticks([0,100])
    ax.set_title(lib_arts_cats[sp])
    ax.axhline(50, c=cb_dark_gray, alpha=0.3)
    if sp == 4:
        ax.tick_params(bottom="off", top="off", left="off", right="off")
    else:
        ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom="off")

    
    if sp == 0:
        ax.text(2007, 19, 'Men')
        ax.text(2005, 76, 'Women')
        
# Generating the third column of graphs
for sp in range(0,6):
    col_index = (3 * sp) + 3
    ax = fig.add_subplot(6,3,col_index)
    ax.plot(women_degrees['Year'], women_degrees[other_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[other_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_yticks([0,100])
    ax.set_title(other_cats[sp])
    ax.axhline(50, c=cb_dark_gray, alpha=0.3)
    if sp == 5:
        ax.tick_params(bottom="off", top="off", left="off", right="off")
    else:
        ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom="off")
    
    if sp == 0:
        ax.text(2007, 5, 'Men')
        ax.text(2005, 91, 'Women')
    elif sp == 5:
        ax.text(2007, 63, 'Men')
        ax.text(2005, 30, 'Women')
# Exports the combined set of graphs as a png file
fig.savefig("gender_degrees.png")
plt.show()


# In[ ]:



