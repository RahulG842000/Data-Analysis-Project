#!/usr/bin/env python
# coding: utf-8

# # HR Data Cleaning 

# In[2]:


import pandas as pd


# In[4]:


df = pd.read_csv("HR Data (1).csv")


# In[25]:


df.head(10)


# In[14]:


df.mean


# In[18]:


unnecessary_columns = ['EmployeeCount', 'EmployeeNumber', 'StandardHours']
df.drop(columns=unnecessary_columns, inplace=True)


# # ensure unnecessary column remove

# In[19]:


df.head()


# # No need to change column Name

# # Standardize the values in the 'Gender' column

# In[22]:


df['Gender'] = df['Gender'].apply(lambda x: x.lower() if x in ['Male','Female'] else 'unknown')


#  # Drop rows with any NaN values

# In[23]:


df.dropna(inplace=True)


# In[26]:


df.head()


# In[27]:


df.to_csv('cleaned_dataset.csv', index=False)


# In[ ]:




