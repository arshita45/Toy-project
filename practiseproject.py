# -*- coding: utf-8 -*-
"""practiseproject.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XHiDXEViRG8YWitN9eyZVnqUUzZ21crV
"""

import pandas as pd
import numpy as np

"""pandas has a dataframe which we are naming as pd here and numpy is the library used for making n dimensional arrays in ml"""

df = pd.read_csv('/placement.csv')

"""shape function defines how many rows and columns are there in my dataset wheras info function in pandas helps us to check the info in each column whether its there are any null values or not"""

df.shape

df.info()

df.head()

"""our first step is preprocessing to remove unwanted data columns etc here one column is extra so we are keeping all the rows and taking column from 1 index onwards"""

df = df.iloc[:,1:]

df.head()

import matplotlib.pyplot as plt

"""second step is eda in which study our datastep here we are plotting it in a graph to know which model to apply c means colour through graph we can see that logistic regression can be applied a single line can be drawn and thirs step was feature selection

"""

plt.scatter(df['cgpa'], df['iq'] , c=df['placement'])

"""x axis is cgpa and y axis is iq and c means it will colour them on basis of placement"""

x= df.iloc[:,[0,2]]
y = df.iloc[:,-1]

x

y

"""previous step was  extracting input and output columns x is the independent variable 2d tensor and y is dependent varibale 1d tensor"""

from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.1)

"""next step is scaling the data"""

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)

x_test = scaler.transform(x_test)

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

clf.fit(x_train,y_train)

y_pred= clf.predict(x_test)

y_test

from sklearn.metrics import accuracy_score

accuracy_score(y_test,y_pred)

"""fit keyword is used as model learn from it in case od preprocessing tool like standardscaler it calculates mean and standard deviation for each feature and store it in scaler and this happens in training data

and in case of algorithms fit calculates the like in logistic regression it calculates the bestfit line and learn the pattren in training data
"""

import pickle

pickle.dump(clf,open('model.pkl','wb'))