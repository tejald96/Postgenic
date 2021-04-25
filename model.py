#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the standard Packages
import numpy as np
import pandas as pd


# In[2]:


#Reading the CSV file and allocating the file under the name insta
insta = pd.read_excel('Data_Cleaned_Instagram_V02.xlsx')
insta


# In[3]:


insta1 = insta.drop(['USERNAME','DATE','Floor Time'], axis=1)
insta1


# In[4]:


X1 = insta1.iloc[:, 0:-1].values
y1 = insta1.iloc[:, -1].values 
#Splitting the data into 20% testing and 80% training data.

# Importing the train_test_split from sklearn.model_selection
from sklearn.model_selection import train_test_split

X1_train,X1_test,y1_train,y1_test=train_test_split(X1,y1,test_size=0.05,random_state=567)


# In[5]:


#Splitting the data into 65% training and 15% validation.
X1_train1,X1_val,y1_train1,y1_val=train_test_split(X1_train,y1_train,test_size=0.80,random_state=567)


# In[11]:



# In[17]:


# importing the standard packages
from xgboost import XGBClassifier
import xgboost as xgb


# In[18]:


#XGB Classifier:
for i in range(5, 12, 2):
    from xgboost import XGBClassifier
    xgclf=XGBClassifier(n_estimators=i)
    xgclf.fit(X1_train1,y1_train1)

import pickle

pickle.dump(xgclf, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))


# In[ ]:




