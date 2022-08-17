#!/usr/bin/env python
# coding: utf-8

# In[7]:


#IMPORT PANDAS AND READ IN THE ECOOMMERCE PURCHASES CSV FILE AND SET IT TO A DATAFRAME CALLED ECOM


# In[8]:


import pandas as pd


# In[9]:


ecom=pd.read_csv("C:\\Users\\LAKSHMI\\Downloads\\Ecommerce Purchases.csv")
ecom


# In[10]:


#HEAD OF THE DATAFRAME


# In[11]:


ecom.head()


# In[12]:


#PRINT HOW MANY ROWS AND COLOUMS IN DATASET


# In[13]:


ecom.info()


# In[14]:


#AVERAGE PURCHASE PRICE


# In[15]:


ecom['Purchase Price'].mean()


# In[16]:


#HIGHEST AND LOWEST PURCHASE PRICES


# In[17]:


ecom["Purchase Price"].max()


# In[18]:


ecom["Purchase Price"].min()


# In[19]:


#PEOPLE WHO HAVW ENGLISH "en" AS THEIR LANGUAGE ON THE WEBSITE


# In[21]:


ecom[ecom['Language']=='en'].count()


# In[ ]:


#PEOPLE WHO HAVE THE JOB OF"Layer"


# In[22]:


ecom[ecom['Job']=='Lawyer'].info()


# In[24]:


#PEOPLE WHO MADE THE PURCHASE DURING THE AM AND PEOPLE WHO MADE THE PURCHASE DURING "PM"
ecom['AM or PM'].value_counts()


# In[ ]:


# MOST 5 COMMON JOB TITLES


# In[26]:


ecom['Job'].value_counts().head()


# In[ ]:


# WHO PURCHASE THAT CAME FROM LOT:"90 WT",AND PRUCHASE PRICE FOR THIS TRANSACTION


# In[29]:


ecom[ecom['Lot']=='90 WT']['Purchase Price']


# In[ ]:


# email of the person with the following credit card number:4926535242672853**


# In[32]:


ecom[ecom['Credit Card']==4926535242672853]['Email']


# In[ ]:


# people have American express as their credit card provider and made a purchase above $95


# In[39]:


ecom[(ecom['CC Provider']=='American Express')&(ecom['Purchase Price']>95)].count()


# In[ ]:


#how many people have a credict card and expires in 2025


# In[40]:


sum(ecom['CC Exp Date'].apply(lambda x:x[3:])=='25')


# In[41]:


#Hard: What are the top5 most popular email providers/hosts (e.g.gmail.com,yahoo.com,etc...)


# In[43]:


ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head()


# In[ ]:




