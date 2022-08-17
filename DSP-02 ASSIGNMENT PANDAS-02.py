#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


#read salaries.csv as a dataframe called sal


# In[3]:


sal=pd.read_csv('C:\\Users\\LAKSHMI\\Downloads\\Salaries.csv')
sal


# In[ ]:


#head of the dataframe


# In[4]:


sal.head()


# In[ ]:


#info() method


# In[5]:


sal.info()


# In[ ]:


#average basepay


# In[7]:


sal['BasePay'].mean()


# In[ ]:


#hightest amount of overtime pay in the dataset


# In[9]:


sal['OvertimePay'].max()


# In[ ]:


#job title of JOSEPH DRISCOLL 


# In[11]:


sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']


# In[ ]:


# JOSEPH DRISCOLL make including benifits


# In[13]:


sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']


# In[ ]:


#name of the highest paid person including benifits


# In[15]:


sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]


# In[ ]:


# lowest paid person includind benifits and how much he and she paid


# In[16]:


sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]


# In[ ]:


#average basepay of all employees per year(2011-2014)


# In[20]:


sal.groupby('Year').mean()['BasePay']


# In[ ]:


#unique job titles


# In[21]:


sal['JobTitle'].nunique()


# In[ ]:


#top 5 most common jobs


# In[26]:


jobs=sal.groupby('JobTitle').count()
top_five=jobs.sort_values(by='Id',ascending=False)[:5]
top_five['Id']


# In[27]:


#jobtitle were represents by only one person in 2013


# In[29]:


year=sal[sal['Year']==2013]
group=year.groupby('JobTitle').count()
count=group[group['Id']==1]
count.count()['Id']


# In[30]:


#word chief in the jobtitle


# In[31]:


def go_chief(job_title):
    if 'cheif' in job_title.lower().split():
        return True
    else:
        return False


# In[32]:


df=pd.read_csv('C:\\Users\\LAKSHMI\\Downloads\\Salaries.csv')


# In[34]:


sum(df['JobTitle'].apply(lambda x: go_chief(x)))


# In[36]:


sal['title_len']=sal['JobTitle'].apply(len)


# In[37]:


#Is there any correlation between length of the Job title string and salary


# In[38]:


sal[['title_len','TotalPayBenefits']].corr()


# In[ ]:




