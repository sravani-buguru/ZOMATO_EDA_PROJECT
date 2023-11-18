#!/usr/bin/env python
# coding: utf-8

# # Zomato Dataset Exploratory Data Analysis

# In[107]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[106]:


df=pd.read_csv('zomato.csv',encoding='latin-1')
df.head()


# In[3]:


df.columns


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.shape


# # Finding missing values

# In[7]:


df.isnull().sum()


# # finding missing values using list comprehension

# In[9]:


[features for features in df.columns if df[features].isnull().sum()>0]


# # finding missing values using heatmaps

# In[63]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[16]:


df_country=pd.read_excel('Country-Code.xlsx')
df_country.head()


# In[17]:


df.columns


# In[ ]:


#combining 2 columns for 2 different data set


# In[18]:


final_df=pd.merge(df,df_country,on='Country Code',how='left')
final_df.head(2)


# In[ ]:


#checking data types


# In[19]:


final_df.dtypes


# In[20]:


final_df.columns


# In[ ]:


# trying to find out how many different countries are there and respect to that particular country how many records are there 


# In[27]:


final_df.Country.value_counts()


# In[28]:


final_df.Country.value_counts().index


# In[30]:


country_names=final_df.Country.value_counts().index


# In[37]:


final_df.Country.value_counts().values


# In[38]:


country_val=final_df.Country.value_counts().values


# In[ ]:


#Pie Chart- Top 3 countries uses Zomato


# In[40]:


plt.pie(country_val[:3],labels=country_names[:3],autopct='%1.2f%%')


# OBSERVATION: India(94.39%)  has more Zomato transactions following up by United States(4.73%) and Uinted Kingdom(0.87%)

# In[42]:


final_df.columns


# In[50]:


final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[53]:


ratings=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[54]:


ratings

# OBSERVATION
When rating is between 4.5 to 4.9 is excellent
When rating id between 4.0 to 4.4 is very good
When rating is between 3.5 to 3.9 is good
When rating is between 2.5 to 3.4 is average
When rating is between 0.0 to 2.4 is poor

# In[55]:


ratings.head()


# In[62]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(12,16)
sns.barplot(x="Aggregate rating",y="Rating Count",data=ratings)


# In[73]:


sns.barplot(x="Aggregate rating",y="Rating Count",hue='Rating color',data=ratings)


# OBSERVATION
#    1. Not Rated count is very high
#    2. maximum number of ratings is between 2.5 to 3.4

# In[66]:


sns.barplot(x="Rating color",y="Aggregate rating",data=ratings)


# In[ ]:


#count plot


# In[71]:


sns.countplot(x='Rating color',data=ratings)


# In[74]:


ratings


# In[ ]:


#find the countries name that has given 0 rating


# In[75]:


final_df.columns


# In[79]:


final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index()


# OBSERVATION
# Maximum number of 0 ratings are from India

# In[80]:


#find out which currency is used by which country?
final_df.columns


# In[81]:


final_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()


# In[ ]:


#which countries do have online deliveries option


# In[84]:


final_df[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()


# # observation
# 1.online deleveries are available in India and UAE

# In[ ]:


#creating pie chart forTop 5 cities distribution


# In[86]:


final_df.City.value_counts().index


# In[92]:


city_values=final_df.City.value_counts().values
city_labels=final_df.City.value_counts().index


# In[94]:


plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.2f%%')


# OBSERVATION :
# Maximum number of transactions is happening from New Delhi

# In[96]:


final_df[['Cuisines','Country']].groupby(['Cuisines','Country']).size().reset_index()

