#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing necessary libraries
import pandas as pd # To manage data as data frames
import numpy as np # To manipulate data as arrays
from sklearn.linear_model import LogisticRegression # Classification model


# In[2]:


url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
data = pd.read_csv(url)
data.head()


# In[3]:


#Dictionary to change the variety variable to numeric
variety_mappings={0:'Setosa', 1:'Versicolor', 2:'Virginica'}

#Encoding the variables
data=data.replace(['Setosa','Versicolor','Virginica'],[0,1,2])


# In[4]:


#Separate the undependent variables, X from the dependent variable, Y
x=data.iloc[:, 0:-1] #excludes the last column
y=data.iloc[:, -1] #The last column


# In[5]:


#Running a logistic regression
logreg = LogisticRegression(max_iter=1000)
logreg.fit(x,y)


# In[6]:


#Building a model based on the inputs and running the prediction
def classify(a,b,c,d): #the four inputs
    arr=np.array([a,b,c,d]) #converting the inputs to a dataframe
    arr=arr.astype(np.float64) #assigning the imputs float data type
    query=arr.reshape(1,-1) #reshaping the array
    prediction=variety_mappings[logreg.predict(query)[0]] #retrieving the data from the query
    return prediction


# In[ ]:




