#!/usr/bin/env python
# coding: utf-8

# data cleaning

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df=pd.read_csv(r'C:\Users\ritika shukla\Downloads\archive (3)\hotel_booking.csv')


# In[3]:


df.columns


# In[4]:


df.drop(['name','email','phone-number','credit_card','company','children','babies'], axis='columns', inplace=True)


# In[5]:


df.head(100)
df.tail()


# In[6]:


df.head()


# In[7]:


df.info()


# In[8]:


df['reservation_status_date']=pd.to_datetime(df['reservation_status_date'])
df.head()


# In[9]:


df.info()


# In[10]:


df.describe(include='object')


# In[11]:


df.describe()


# In[12]:


df=df[df['adr']<5000]
df.info()


# In[13]:


df.describe()


# In[14]:


df['agent'].fillna(0,inplace=True)
df['country'].fillna('x' ,inplace=True)


# In[15]:


df.head(100)
df.info()


# Data Visualization
# 

# In[16]:


canceled= df['is_canceled'].value_counts(normalize=True)
print(canceled)


# In[17]:


canceled=sns.catplot(data=df, kind='count', x='is_canceled',hue='hotel', height=4, aspect=2, palette='Accent')
canceled.set_xticklabels(['not_canceled','canceled'])
plt.title("Cancelation Rate")
plt.show()


# In[18]:


City_hotel_cancelation= df[df['hotel']=='City Hotel']
City_hotel_cancelation['is_canceled'].value_counts(normalize=True)


# In[19]:


Resort_hotel_cancelation= df[df['hotel']=='Resort Hotel']
Resort_hotel_cancelation['is_canceled'].value_counts(normalize=True)


# In[20]:


Resort_hotel = Resort_hotel_cancelation.groupby('reservation_status_date')[['adr']].mean()
City_hotel = City_hotel_cancelation.groupby('reservation_status_date')[['adr']].mean()


# In[21]:


sns.set({'figure.figsize': (15,5)})
sns.lineplot(data=Resort_hotel, x=Resort_hotel.index, y=Resort_hotel['adr'], label='Resort Hotel')
sns.lineplot(data=City_hotel, x=City_hotel.index, y=City_hotel['adr'], label='City Hotel')
plt.legend(fontsize=10)
plt.show()


# In[22]:


plt.title('Reservation Status Per Month')
df['month']= df['reservation_status_date'].dt.month
sns.countplot(x='month', hue='is_canceled', data=df)
plt.show()


# In[23]:


plt.title('ADR per month')
sns.barplot(x='month', y='adr', data=df[df['is_canceled']==1].groupby('month')[['adr']].sum().reset_index())
plt.show()


# In[24]:


sns.set({'figure.figsize' :(5,5)})
plt.title("Highest Cancelled Reservation In Countries")
canceled_data = df[df['is_canceled']==1]
top_10_country=canceled_data['country'].value_counts()[:5]
plt.pie(top_10_country, autopct='%.2f', labels=top_10_country.index)
plt.show()


# In[25]:


sns.set({'figure.figsize' :(5,5)})
market_segment_percent=((df['market_segment'].value_counts()/df['market_segment'].value_counts().sum())*100)
print(market_segment_percent[:5])
plt.pie(market_segment_percent, autopct='%.2f%%', labels= market_segment_percent.index)
plt.show()


# In[26]:


sns.set({'figure.figsize' :(5,5)})
market_segment_percent=(canceled_data['market_segment'].value_counts()/canceled_data['market_segment'].value_counts().sum())*100
print(market_segment_percent[:5])
patches, texts, autotexts=plt.pie(market_segment_percent, autopct='%.2f%%', labels= market_segment_percent.index)
patches[6].set_visible(False)
texts[6].set_visible(False)
autotexts[6].set_visible(False)
patches[5].set_visible(False)
texts[5].set_visible(False)
autotexts[5].set_visible(False)
plt.show()


# In[59]:


not_canceled_data = df[df['is_canceled']==0]
not_canceled_data_adr= non_canceled_data.groupby('reservation_status_date')[['adr']].mean()
not_canceled_data_adr.reset_index(inplace=True)
not_canceled_data_adr.sort_values('reservation_status_date', inplace=True)

canceled_data = df[df['is_canceled']==1]
canceled_data_adr= canceled_data.groupby('reservation_status_date')[['adr']].mean()
canceled_data_adr.reset_index(inplace=True)
canceled_data_adr.sort_values('reservation_status_date', inplace=True)

plt.figure(figsize=(20,6))
plt.title("Daily ADR Rate")
plt.plot(not_canceled_data_adr['reservation_status_date'], not_canceled_data_adr['adr'], label='not canceled')
plt.plot(canceled_data_adr['reservation_status_date'], canceled_data_adr['adr'], label='canceled')
plt.legend(fontsize=20)
plt.show()


# In[58]:


not_canceled_data_adr=not_canceled_data_adr[(not_canceled_data_adr['reservation_status_date']>'2016') & (not_canceled_data_adr['reservation_status_date']<'2017-09')]
canceled_data_adr=canceled_data_adr[(canceled_data_adr['reservation_status_date']>'2016') & (canceled_data_adr['reservation_status_date']<'2017-09')]
plt.figure(figsize=(20,6))
plt.title("Daily ADR Rate")
plt.plot(not_canceled_data_adr['reservation_status_date'], not_canceled_data_adr['adr'], label='not canceled')
plt.plot(canceled_data_adr['reservation_status_date'], canceled_data_adr['adr'], label='canceled')
plt.legend(fontsize=20)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




