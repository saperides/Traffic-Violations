#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
os.chdir('C:\\Users\\M246047\\Documents\\Python')
import numpy as np
import pandas as pd
import datetime as dt
import pylab
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import scipy as sc
from scipy.stats import ttest_ind
import re
import seaborn as sns
import scipy.stats as stats


# In[26]:


testing = pd.read_csv('student_testing.csv')
testing = pd.DataFrame(testing)
print(testing.columns)
print('\n', testing.describe())


# In[13]:


print(testing.head())
print(testing.dtypes)


# In[63]:


math = testing[['math score']]
math_scores = math.iloc[:, 0]
reading = testing[['reading score']]
reading_scores = reading.iloc[:, 0]
writing = testing[['writing score']]
writing_scores = writing.iloc[:, 0]


plt.hist([math_scores, reading_scores, writing_scores], bins=20, label=['Math Scores', 'Reading Scores', 'Writing Scores'])
plt.legend(loc='upper right')
plt.show()

# fig, ax = plt.subplots()
# math_heights, math_bins = np.histogram(testing['math score'])
# reading_heights, reading_bins = np.histogram(reading['reading score'], bins=math_bins)
# writing_heights, writing_bins = np.histogram(writing['writing score'], bins=math_bins)

# width = (math_bins[1] - math_bins[0])/3
# ax.bar(math_bins[:-1], math_heights, width=width, alpha=.5, facecolor='cornflowerblue')
# ax.bar(reading_bins[:-1]+width, reading_heights, width=width, alpha=.5, facecolor='seagreen')
# ax.bar(writing_bins[:-1]+width, writing_heights, width=width, alpha=.5, facecolor='pink')
# #seaborn.despine(ax=ax, offset=10)
  
# plt.xlabel('Test Scores')
# plt.legend(loc='upper right')
# plt.title('Student Test Scores')
# plt.show()


# In[65]:


parent_ed = testing.groupby('parental level of education')['math score'].mean()
print(parent_ed[:5])

print(testing.groupby('lunch')['math score'].mean())
sns.catplot(x='lunch', y='math score', size=6, kind='boxen', data=testing)
sns.catplot(x='lunch', y='reading score', size=6, kind='boxen', data=testing)
sns.catplot(x='lunch', y='writing score', size=6, kind='boxen', data=testing)


# In[69]:


free_reduced = testing.loc[testing['lunch'] == 'free/reduced']
lunch = testing.loc[testing['lunch'] == 'standard']
free_reduced_math = free_reduced['math score']
lunch_math = lunch['math score']

t_val = stats.ttest_ind(free_reduced_math, lunch_math)
print('Statistic tests for students with lunch assistance vs those without: \n ', t_val)


# Lower test scores reflect poorly on schools and decrease student morale. Increasing test scores would increase student confidence and potentially lead to additional opportunities in school and upon graduation. While we know tests don't accurately measure an individual's level of intelligence, a child who consistently does poorly on tests may sincerely believe they are incapable which may hinder them from reaching their full potential. 
# 
# It is often said that breakfast is the most important meal of the day. How does having or missing breakfast affect student test scores? I believe that starting the day with a nutrient-rich breakfast will increase test scores. 
# 
# In a perfect world, we would feed half the students a particular breakfast at school in the morning and have the other half come to school without having eaten. This may be taken negatively, so I might propose adding a simple yes or no question to every test: Have you eaten breakfast this morning? The variable of interest is test scores in breakfast and non-breakfast groups, and this would be an A/B manipulation where breakfast is eaten or not eaten. We may also be able to run a chi-square test on the data. 
# 
# To start this study, I would take a survey of the students asking who does and does not eat breakfast in the morning and compare the test scores of those two groups. I would then randomly choose 20% of the students who reported they do not eat breakfast to begin eating breakfast in the mornings. If after three tests scores increase by at least 10%, I would conclude that eating breakfast is positively impactful to student life and would request that all students eat breakfast before or at school in the morning. If after three tests scores increase but by less than 10%, I would observe for another three tests. If test scores do not increase by after three tests, I would conclude that eating breakfast is not impactful and allow students to return to their regular routine. 

# In[ ]:




