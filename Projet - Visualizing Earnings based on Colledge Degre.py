#!/usr/bin/env python
# coding: utf-8

# ## Project : Analyzing job outcome of students
# In this project, we'll be working with a dataset on the job outcomes of students who graduated from college between 2010 and 2012. The original data on job outcomes was released by American Community Survey, which conducts surveys and aggregates the data. The dataset is cleaned and released on their Github repo.
# 
# Each row in the dataset represents a different major in college and contains information on gender diversity, employment rates, median salaries, and more. Here are some of the columns in the dataset:
# 
# - Rank - Rank by median earnings (the dataset is ordered by this column).
# - Major_code - Major code.
# - Major - Major description.
# - Major_category - Category of major.
# - Total - Total number of people with major.
# - Sample_size - Sample size (unweighted) of full-time.
# - Men - Male graduates.
# - Women - Female graduates.
# - ShareWomen - Women as share of total.
# - Employed - Number employed.
# - Median - Median salary of full-time, year-round workers.
# - Low_wage_jobs - Number in low-wage service jobs.
# - Full_time - Number employed 35 hours or more.
# - Part_time - Number employed less than 35 hours.
# 
# 
# 
# 
# 

# In[50]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[51]:


#Read the grads data
recent_grads = pd.read_csv('recent-grads.csv')


# In[52]:


#Explore the firse row 
recent_grads.iloc[0]


# In[53]:


#Explore the data
print(recent_grads.head())


# In[54]:


print(recent_grads.tail())


# In[55]:


#Get the data statistics
recent_grads.describe()


# In[56]:


#Drop rows with missing values
recent_grads = recent_grads.dropna()


# ## Pandas Scatter Plots

# In[57]:


#Ploting / Looking for correlations 
recent_grads.plot(x='Sample_size', y='Median', kind='scatter')


# Overall grads are payed between 20K and 80K.
# We have outliers on the sample size axis.

# In[58]:


recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter')


# For all sampe sizes, the unployment rate are between 0 and 0.2

# In[59]:


recent_grads.plot(x='Full_time', y='Median', kind='scatter')


# Salary median is between 20k and 80K. No evidence if you work full time that the salary is higher.

# In[60]:


recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter')


# The women share of unemployement is higher the men's share

# In[61]:


recent_grads.plot(x='Men', y='Median', kind='scatter')


# In[62]:


recent_grads.plot(x='Women', y='Median', kind='scatter')


# Men are paid slightly higher than women

# ## Pandas Histogram Plots

# In[84]:


#Explore distributions 
cols = ["Sample_size", "Median","ShareWomen", "Unemployment_rate", "Men", "Women"]

fig = plt.figure(figsize=(15,12))
for r in range(1,5):
    ax = fig.add_subplot(2,2,r)
    ax = recent_grads[cols[r]].plot(kind='hist', rot=0)
    ax = plt.xlabel(cols[r])


# - The overal salariers are between 20k and 60K. (maximum between 30K and 40K)
# - Full-time jobs are high
# - The women share of unemployment is high

# ## Pandas, Scatter Matrix Plot¶
# 

# In[91]:


# Looking for relations and correlations between columns
from pandas.plotting import scatter_matrix
scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']], figsize=(10,10))


# ## Pandas, Bar Plots¶
# 

# In[93]:


# Women share in different Majors
recent_grads[:10].plot.bar(x='Major', y='ShareWomen', legend=False) ## first ranked majors
recent_grads[163:].plot.bar(x='Major', y='ShareWomen', legend=False) ## least ranked majors


# In[ ]:




