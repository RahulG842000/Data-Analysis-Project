#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[10]:


df = pd.read_csv('Diwali Sales Data.csv' , encoding= 'unicode_escape')


# In[11]:


df.shape


# In[12]:


df.head()


# In[13]:


df.info()


# In[14]:


df.drop(['Status', 'unnamed1'], axis = 1, inplace = True)


# In[15]:


pd.isnull(df)


# In[16]:


pd.isnull(df).sum()


# In[17]:


df.shape


# In[18]:


df.dropna(inplace = True)


# In[19]:


df["Amount"] =df["Amount"].astype('int')


# In[20]:


df["Amount"].dtype


# In[22]:


df.columns


# In[23]:


df.describe()


# # Exploratory Data Analysis

# Gender

# In[24]:


ax = sns.countplot(x = "Gender",data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[26]:


df.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending=False)


# In[28]:


sales_gen = df.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
sns.barplot(x = 'Gender', y= 'Amount' , data = sales_gen)


# from Above ghaphs we can see thatmost of the buyers are females and even the purchasing power of females are greater than man

# # Age

# In[29]:


ax = sns.countplot(data = df, x = 'Age Group', hue = "Gender")

for bars in ax.containers:
    ax.bar_label(bars)


# In[33]:


sales_age = df.groupby(["Age Group"], as_index = False)["Amount"].sum().sort_values(by ='Amount', ascending = False)

sns.barplot (x= 'Age Group',y= "Amount" ,data = sales_age)


# from above graph we can see that most of the buyers are Age group between 26-35 years female

# In[40]:


sales_State = df.groupby(["State"], as_index = False)["Orders"].sum().sort_values(by ='Orders', ascending = False).head(10)

sns.set(rc= {"figure.figsize":(15,5)})

sns.barplot (data = sales_State, x= 'State',y= "Orders")


# In[41]:


sales_State = df.groupby(["State"], as_index = False)["Amount"].sum().sort_values(by ='Amount', ascending = False).head(10)

sns.set(rc= {"figure.figsize":(15,5)})

sns.barplot (data = sales_State, x= 'State',y= "Amount")


# from Above Graphs we can see that most of the orders 7 Total sales/amount are Utter Pradesh , Maharashtra, and karnataka respectively

# In[45]:


ax  = sns.countplot (data =df, x= 'Marital_Status')

sns.set(rc= {"figure.figsize":(6,5)})


for bars in ax.containers:
    ax.bar_label(bars)


# In[46]:


sales_State = df.groupby(["Marital_Status", "Gender"], as_index = False)["Amount"].sum().sort_values(by ='Amount', ascending = False)

sns.set(rc= {"figure.figsize":(6,5)})

sns.barplot (data = sales_State, x= 'Marital_Status',y= "Amount", hue = 'Gender')


# From Above Graphs we can see that most of the buyers are married (women) and they have high purchase power

# # Occupation

# In[47]:


sns.set(rc= {"figure.figsize":(20,5)})

ax = sns.countplot (data = df, x= 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[48]:


sales_State = df.groupby(["Occupation"], as_index = False)["Amount"].sum().sort_values(by ='Amount', ascending = False)

sns.set(rc= {"figure.figsize":(20,5)})

sns.barplot (data = sales_State, x= 'Occupation',y= "Amount",)


# From Above Graphs we can see that most of the buyers are working in IT, Aviation, And HealthCare sector

# In[52]:


sns.set(rc= {"figure.figsize":(25,5)})

ax = sns.countplot (data = df, x= 'Product_Category')


for bars in ax.containers:
    ax.bar_label(bars)


# In[55]:


sales_State = df.groupby(["Product_Category"], as_index = False)["Amount"].sum().sort_values(by ='Amount', ascending = False).head(10)

sns.set(rc= {"figure.figsize":(25,5)})

sns.barplot (data = sales_State, x= 'Product_Category',y= "Amount",)


# From Above graphs we can see that most of the sold product Are from Food , Footwear , And Electronic Category

# In[57]:


sales_State = df.groupby(["Product_ID"], as_index = False)["Orders"].sum().sort_values(by ='Orders', ascending = False).head(10)

sns.set(rc= {"figure.figsize":(20,5)})

sns.barplot (data = sales_State, x= 'Product_ID',y= "Orders",)


# # Conclusion:

# married women age Group 26-35 yrs from UP, Maharashtra and Karnataka working in IT, Healthcare and Aviation are more likely buy prodct from food clothing And Electronic Category
