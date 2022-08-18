#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
x=np.arange(0,100)
y=x*2
z=x**2


# In[ ]:


#import matplotlib.pyplot as plt and set % matplotlib you aren't using the jyupyter notebookib inline if you are using the jyupyter notebook.what command do you use if 


# In[3]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib','inline')


# In[ ]:


#create a figure object called fig using plt.figure()
#use add_axes to add an axis to the figure canvas at[0,0,1,1].call this new axis ax


# In[4]:


fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')


# In[ ]:


#create a figure object and put two axes on it,ax1 and ax2.loacated at[0,0,1,1]and [0.2,0.5,0.2,0.2]respectivily


# In[7]:


fig=plt.figure()
ax1=fig.add_axes([0,0,1,1])
ax2=fig.add_axes([0.2,0.5,0.2,0.2])


# In[ ]:


#plot(x,y) on both axes.and call your figure object to show it


# In[10]:


ax1.plot(x,y)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax2.plot(x,y)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
fig


# In[ ]:


#create the plot below by adding two axes to a figure object at[0,0,1,1]and[0.2,0.5,0.4,0.4]


# In[12]:


fig=plt.figure()
ax1=fig.add_axes([0,0,1,1])
ax2=fig.add_axes([0.2,0.5,0.4,0.4])


# In[ ]:


#now use x,y and z arrays to recreate the plot below notice the xlimits and y limits on the inserted plot


# In[13]:


ax1.plot(x,z)
ax1.set_xlabel('x')
ax2.set_ylabel('z')
ax2.plot(x,y)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('zoom')
ax2.set_xlim(20,22)
ax2.set_ylim(30,50)
fig


# In[ ]:


#use plt.subplots(nrows=1,ncols=2)to create the plot 


# In[14]:


fig, axes=plt.subplots(nrows=1,ncols=2)


# In[ ]:


#plot(x,y) and (x,z) on the axes.play around with the linewidth and style


# In[17]:


axes[0].plot(x,y,color="blue",lw=3,ls='--')
axes[1].plot(x,y,color="red",lw=3,ls='-')
fig


# In[ ]:


#adding the figsize() argument in plt.subplots() are copying and pasting your previous code


# In[20]:


fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(12,2))
axes[0].plot(x,y,color="blue",lw=5)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[1].plot(x,z,color="red",lw=3,ls='--')
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')


# In[ ]:




