
# coding: utf-8

# In[1]:


import os
import pandas as pd
os.chdir("e:\working folder")
os.getcwd()

sns = pd.read_csv('snsdata.csv')
sns.head(6)


# In[2]:


print("Average age is %d"%sns['age'].mean(skipna=True))
print("Is there any null value in age data?", pd.isnull(sns['age']).sum()>0)


# In[3]:


#how to fill NAs with zero


sns.fillna(0, inplace=True)
averageval=sns['age'].mean(skipna=True)
averageval=round(averageval,2)
print(averageval)
print("Now the average age is %d" %averageval)
sns.head(6)



# In[4]:


#Replace missing values and NAs with some numbers

filename = "snsdata.csv"
sns1 = pd.read_csv("snsdata.csv")
sns1.fillna({'age': 19, 'gender': 'F'}, inplace=True)
sns1.head(6)


# In[5]:


#Replace NAs with mean

filename = "snsdata.csv"
sns2 = pd.read_csv("snsdata.csv")
sns2.fillna({'age': sns2['age'].mean(skipna=True)}, inplace=True)
sns2['age'].head(6)


# In[6]:


#replace NAs with the median in age

filename = "snsdata.csv"
sns3 = pd.read_csv("snsdata.csv")
sns3.fillna({'age': sns3['age'].median(skipna=True)}, inplace=True)
sns2['age'].head(6)


# In[7]:


#to check the number of rows and columns

sns.shape


# In[8]:


#To check the data type of the data frame

sns.dtypes


# In[9]:


#to write on the numeric columns of the data frame

num_cols=['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
sns.select_dtypes(include=num_cols).head(6)


# In[10]:


#who to return only categorical columns from the given data frame
#dataframe.select_dtypes(include=none, exclude=none)

sns.select_dtypes(include=['object'])


# In[11]:


#How to check the name of numeric columns

sns._get_numeric_data().columns


# In[12]:


#How to check the name of numeric columns

sns.select_dtypes(exclude=num_cols).columns


# In[13]:


#find the SD of the numeric columns


sns._get_numeric_data().std()


# In[14]:


sns[sns._get_numeric_data().columns].std()


# In[15]:


#Describing data 
sns.describe()


# In[122]:


#Displaying data with filter

sns[sns.gradyear == 2007].describe()


# In[123]:


sns[sns.gradyear == sns['gradyear'].max()].describe()


# In[127]:


#Display stats of selected Rows & Columns

sns[['gradyear', 'age','friends']][sns.gradyear==sns['gradyear'].max()]

