# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:06:48 2020

@author: Nidhi
"""



#importing librabries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
heartdata = pd.read_csv("heartd.csv") 
heartdata.head()
#ap_hi-systolic
#ap_low-diastolic




#counts number of empyt value in each coulmn
heartdata.isnull().sum()




#view some basic statistic
heartdata.describe()




#Get the count of number of patients with and without heart disease
print(heartdata['target'].value_counts())
sns.countplot(heartdata['target'])





pd.crosstab(heartdata.age,heartdata.target).plot(kind="bar",figsize=(20,6))
plt.title('Heart Disease Frequency for Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()




heartdata.corr()


# In[57]:


plt.figure(figsize=(9,9))
sns.heatmap(heartdata.corr(), annot=True, fmt='.0%')


# In[58]:


# cardio_new = heartdata['cardio']
# heartdata = heartdata.drop('id',axis=1)
# heartdata = heartdata.drop('age',axis=1)
# heartdata = heartdata.drop('cardio',axis=1)
# heartdata['cardio'] = cardio_new
heartdata.head()


# In[59]:


#splitting data in features and target
Y =heartdata.target.values
x1=heartdata.drop(["target"],axis=1)
# X= heartdata.iloc[:, :-1].values
# Y = heartdata.iloc[:,-1].values


# In[60]:


#Normalization 
X = (x1 - np.min(x1))/(np.max(x1)-np.min(x1)).values


# In[61]:


#Spliting traning and testing data
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(X,Y,test_size=0.2, random_state=37)


# In[62]:


#transposition
xtrain = xtrain.T
xtest = xtest.T
ytrain = ytrain.T
ytest = ytest.T
#defining accuries list to store accuracy of different models
models_test_accuracies = {}
models_train_accuracies = {}


# In[63]:


#LR with sklearn
from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()
LR.fit(xtrain.T,ytrain.T)
train_acc = LR.score(xtrain.T,ytrain.T)*100
models_train_accuracies['LogisticRegression'] = train_acc
#print("LogisticRegression Traning Accuracy",train_acc)
print("Logistic Regression Traning Accuracy in % : {:.2f}%".format(train_acc))


# In[64]:


#testing model accuracy on testing data
# arry = [[20228,1,156,85,140,90,3,1,0,0,1]]
#print(LR.predict(xtest.T))
test_acc = LR.score(xtest.T,ytest.T)*100
models_test_accuracies['LogisticRegression'] = test_acc
#print("LogisticRegression Testing Accuracy  : ",test_acc)
print("Logistic Regression Testing Accuracy in % : {:.1f}%".format(test_acc))
models_test_accuracies


# In[65]:


#using random forest classifier
from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators = 10 , criterion = 'entropy' , random_state = 1)
forest.fit(xtrain.T,ytrain.T)


# In[67]:


#testing the model accuracy on training data
train_acc = forest.score(xtrain.T,ytrain.T)*100
models_train_accuracies['RandomForestClassifier'] = train_acc
#print("Random Forest Classifier Traning Accuracy",train_acc)
print("Random Forest Classifier Traning Accuracy in % : {:.2f}%".format(train_acc))


# In[68]:


#testing model accuracy on testing data
# arry = [[20228,1,156,85,140,90,3,1,0,0,1]]
#print(forest.predict(xtest.T))
test_acc = forest.score(xtest.T,ytest.T)*100
models_test_accuracies['RandomForestClassifier'] = test_acc
#print("RandomForestClassifier Testing Accuracy  : ",test_acc)
print("RandomForestClassifier Testing Accuracy in % : {:.1f}%".format(test_acc))
models_test_accuracies


# In[70]:


#Using Decision Tree
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
dtc.fit(xtrain.T,ytrain.T)
train_acc = dtc.score(xtrain.T,ytrain.T)*100
models_train_accuracies['Decsion Tree'] = train_acc
#print("Decsion tree Traning Accuracy",train_acc)
print("Decsion tree Traning Accuracy in  % : {:.2f}%".format(train_acc))


# In[71]:


#Testing model Accuracy on test Data
#print(dtc.predict(xtest.T))
test_acc = dtc.score(xtest.T,ytest.T)*100
models_test_accuracies['Decision Tree'] = test_acc
#print("Decision Tree Test Accuracy ",test_acc)
print("Decision Tree Testing Accuracy Score %: {:.2f}%".format(test_acc))
models_test_accuracies


# In[72]:


#Using kneighbour classigier
from sklearn.neighbors import KNeighborsClassifier
kmodel=KNeighborsClassifier(n_neighbors=2)
kmodel.fit(xtrain.T,ytrain.T)
train_acc = kmodel.score(xtrain.T,ytrain.T)*100
models_train_accuracies['KNN'] = train_acc
#print("KNN Traning Accuracy",train_acc)
print("KNN Traning Accuracy in  % : {:.2f}%".format(train_acc))


# In[74]:


#print(kmodel.predict(xtest.T))
test_acc = kmodel.score(xtest.T,ytest.T)*100
models_test_accuracies['KNN'] = test_acc
#print("KNN Test Accuracy ",test_acc)
print("KNN Testing Accuracy Score %: {:.2f}%".format(test_acc))
models_test_accuracies


# In[75]:


#using Support Vector Machine
from sklearn.svm import SVC
svm = SVC(random_state = 37)
svm.fit(xtrain.T,ytrain.T)
train_acc = svm.score(xtrain.T,ytrain.T)*100
models_train_accuracies['SVM'] = train_acc
#print("SVM Traning Accuracy",train_acc)
print("SVM Traning Accuracy in  % : {:.2f}%".format(train_acc))


# In[77]:


#print(svm.predict(xtest.T))
test_acc = svm.score(xtest.T,ytest.T)*100
models_test_accuracies['SVM'] = test_acc
#print("SVM Testing Accuracy",test_acc)
print("SVM Testing Accuracy in  % : {:.2f}%".format(test_acc))
models_test_accuracies


# In[78]:


#Naive Bayes Algorithm
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(xtrain.T,ytrain.T)
train_acc = nb.score(xtrain.T,ytrain.T)*100
models_train_accuracies['Naive Bayes'] = train_acc
#print("Accuracy of Naive Bayes:",train_acc)
print("Naive Bayes Training Accuracy in %: {:.2f}%".format(train_acc))


# In[79]:


nb.predict(xtest.T)
test_acc = nb.score(xtest.T,ytest.T)*100
models_test_accuracies['Naive Bayes'] = test_acc
#print("Accuracy of Naive Bayes:",test_acc)
print("Naive Bayes Testing Accuracy in %: {:.2f}%".format(test_acc))


# In[80]:


#PLOTTING MODELS TRANING ACCURACY
colors = ["yellow", "green","red","blue","orange","purple"]
sns.set_style("whitegrid")
plt.figure(figsize=(15,5))
plt.yticks(np.arange(0,101,10))

plt.ylabel("Traninig-Accuracy")
plt.xlabel("Algorithms")
sns.barplot(x=list(models_train_accuracies.keys()), y=list(models_train_accuracies.values()), palette=colors)
plt.show()


# In[81]:


#PLOTTING MODELS TESTING ACCURACY
colors = ["yellow", "green","red","blue","orange","purple"]
sns.set_style("whitegrid")
plt.figure(figsize=(15,5))
plt.yticks(np.arange(0,101,10))
plt.ylabel("Testing-Accuracy")
plt.xlabel("Algorithms")
sns.barplot(x=list(models_test_accuracies.keys()), y=list(models_test_accuracies.values()), palette=colors)
plt.show()


# In[50]:


models_test_accuracies

