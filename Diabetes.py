# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:08:25 2020

@author: DELL
"""

import numpy as np
import pandas as pd
import pickle

df=pd.read_csv('E:\Complete ML\XL FILES\diabetes.csv')
df.head()
df.isnull().sum()

def impute_nan(df, variable):
    df[variable]=df[variable].replace(0, np.NaN)
    
for feature in ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']:   
    impute_nan(df, feature) 
df.head()

def replace_nan(df, variable):
    median_val=df[variable].median()
    df[variable]=df[variable].fillna(median_val)
    
for feature in ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']:   
    replace_nan(df, feature) 
df.head()



x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2, random_state=0)


from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(x_train, y_train)


pickle.dump(clf, open('model.pkl', 'wb'))




