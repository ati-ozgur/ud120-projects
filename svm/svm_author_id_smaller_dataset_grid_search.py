#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.grid_search import GridSearchCV


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()





features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 


#########################################################
### your code goes here ###

#########################################################

from sklearn.svm import SVC
clf = SVC(kernel="rbf")


param_grid = [
  {'C': [1, 10, 100, 1000, 10000], 'kernel': ['rbf']},
  {'C': [1, 10, 100, 1000, 10000], 'kernel': ['linear']}
 ]


clf = GridSearchCV(SVC(C=1), param_grid, cv=5)
clf.fit(features_train,labels_train)

print(clf.best_params_)

pred = clf.predict(features_test)




from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print "accuracy_score",acc