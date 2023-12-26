#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_excel(r"C:\Users\USER\Documents\Chat GPT Projects\RAW DATA\Fraud Detection\fraud_detection_dataset.xlsx")


# In[3]:


df.head()


# In[5]:


# Checking for missing values
missing_values = df.isnull().sum()
missing_values


# In[6]:


# Checking data types
data_types = df.dtypes
data_types


# In[7]:


# Statistical summary
statistical_summary = df.describe()
statistical_summary


# ## Anomaly Detection

#  Below we conduct an anomaly detection analysis to uncover potential fraud indicators.

# In[8]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[15]:


# Setting up the visualization
plt.figure(figsize=(15, 10))

# Plotting the distribution of transaction types
plt.subplot(2, 2, 1)
sns.countplot(x='type', data=df)
plt.title('Distribution of Transaction Types')


# In[11]:


# Plotting the amount distribution
plt.subplot(2, 2, 2)
sns.histplot(df['amount'], bins=30, kde=True)
plt.title('Distribution of Transaction Amounts')
plt.xlabel('Amount')
plt.ylabel('Frequency')


# In[12]:


# Plotting the relationship between 'amount' and 'isFraud'
plt.subplot(2, 2, 3)
sns.boxplot(x='isFraud', y='amount', data=df)
plt.title('Transaction Amount vs. Fraudulent Status')


# In[13]:


# Plotting the relationship between 'step' and 'isFraud'
plt.subplot(2, 2, 4)
sns.boxplot(x='isFraud', y='step', data=df)
plt.title('Step vs. Fraudulent Status')

plt.tight_layout()
plt.show()


# In[14]:


# Setting up the visualization
plt.figure(figsize=(15, 10))

# Plotting the distribution of transaction types
plt.subplot(2, 2, 1)
sns.countplot(x='type', data=df)
plt.title('Distribution of Transaction Types')


# In[16]:


# Plotting the amount distribution
plt.subplot(2, 2, 2)
sns.histplot(df['amount'], bins=30, kde=True)
plt.title('Distribution of Transaction Amounts')
plt.xlabel('Amount')
plt.ylabel('Frequency')


# In[17]:


# Plotting the relationship between 'amount' and 'isFraud'
plt.subplot(2, 2, 3)
sns.boxplot(x='isFraud', y='amount', data=df)
plt.title('Transaction Amount vs. Fraudulent Status')


# In[18]:


# Plotting the relationship between 'step' and 'isFraud'
plt.subplot(2, 2, 4)
sns.boxplot(x='isFraud', y='step', data=df)
plt.title('Step vs. Fraudulent Status')

plt.tight_layout()
plt.show()


# In[19]:


# Analyzing outliers in 'amount'
amount_outliers = df[df['amount'] > df['amount'].quantile(0.95)]
amount_outliers


# In[20]:


# Checking for unusual patterns in transaction types
type_counts = df['type'].value_counts()
type_counts


# In[21]:


# Examining if there's a specific time frame where fraud occurs more frequently
step_fraud_counts = df.groupby('step')['isFraud'].sum()
step_fraud_counts


# In[ ]:




