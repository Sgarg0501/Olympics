#!/usr/bin/env python
# coding: utf-8

# # Summer Olympics Data Analysis Assignment

# In[104]:


import pandas as pd
import numpy as np
df=pd.read_csv("Desktop/Project/SummerInternship_Olympics.csv")
df


# ## 1. In how many cities Summer Olympics is held so far?

# In[10]:


a=len(pd.unique(df['City']))
a


# ## 2. Which sport is having most number of Gold Medals so far? (Top 5)

# In[59]:


data=[]
for sport in df['Sport'].unique():
    data.append([sport,len(df[(df['Sport']==sport) & (df['Medal']=='Gold')])])
data

data=pd.DataFrame(data,columns=['Sport','No of Gold Medals'])
data=data.sort_values(by='No of Gold Medals',ascending=False)
data=data.head()
data


# In[60]:


data.plot(x='Sport',y='No of Gold Medals',kind='bar')


# ## 3. Which sport is having most number of medals so far? (Top 5)

# In[65]:


data2=[]
for sport in df['Sport'].unique():
    data2.append([sport,len(df[(df['Sport']==sport)])])
data2

data2=pd.DataFrame(data2,columns=['Sport','No of Medals'])
data2=data2.sort_values(by='No of Medals',ascending=False)
data2=data2.head()
data2


# In[67]:


data2.plot(x='Sport',y='No of Medals',kind='bar')


# ## 4. Which player has won most number of medals? (Top 5)

# In[ ]:


data3=[]
for sport in df['Athlete'].unique():
    data3.append([sport,len(df[(df['Athlete']==sport)])])
data3

data3=pd.DataFrame(data3,columns=['Athlete','No of Medals'])
data3=data3.sort_values(by='No of Medals',ascending=False)
data3=data3.head()
data3


# In[70]:


data3.plot(x='Athlete',y='No of Medals',kind='bar')


# ## 5. Which player has won most number Gold Medals of medals? (Top 5)

# In[71]:


data4=[]
for sport in df['Athlete'].unique():
    data4.append([sport,len(df[(df['Athlete']==sport) & (df['Medal']=='Gold')])])
data4

data4=pd.DataFrame(data4,columns=['Athlete','No of Gold Medals'])
data4=data4.sort_values(by='No of Gold Medals',ascending=False)
data4=data4.head()
data4


# In[72]:


data4.plot(x='Athlete',y='No of Gold Medals',kind='bar')


# ## 6. In which year India won first Gold Medal in Summer Olympics?

# In[123]:


data5=[]
for sport in df['Year'].unique():
    data5.append([sport,(df[(df['Country']=='IND') & (df['Medal']=="Gold")])])
data5

data5=pd.DataFrame(data5,columns=['Year','Gold Medal'])
data5=data5.sort_values(by='Year',ascending=True)
data5=data5.head()
data5
data5=data5.head(1)
data5=data5['Year']
data5


# ## 7. Which event is most popular in terms on number of players? (Top 5)

# In[95]:


data6=[]
for sport in df['Event'].unique():
    data6.append([sport,len(df[(df['Event']==sport)])])
data6

data6=pd.DataFrame(data6,columns=['Event','No of Players'])
data6=data6.sort_values(by='No of Players',ascending=False)
data6=data6.head()
data6


# In[97]:


data6.plot(x='Event',y='No of Players',kind='bar')


# ## 8. Which sport is having most female Gold Medalists? (Top 5)

# In[106]:


data7=[]
for sport in df['Sport'].unique():
    data7.append([sport,len(df[(df['Sport']==sport) & (df['Medal']=='Gold') & (df['Gender']=='Women')])])
data7

data7=pd.DataFrame(data7,columns=['Sport','No of Gold Medals Won by Women'])
data7=data7.sort_values(by='No of Gold Medals Won by Women',ascending=False)
data7=data7.head()
data7


# In[108]:


data7.plot(x='Sport',y='No of Gold Medals Won by Women',kind='bar')

