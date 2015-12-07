import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()



#################################################################################


########################## DECISION TREE #################################



#### your code goes here

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

clf = DecisionTreeClassifier(min_samples_split=50)
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
acc_min_samples_split_50 = accuracy_score(pred, labels_test)
print "acc_min_samples_split_50",acc_min_samples_split_50


clf = DecisionTreeClassifier(min_samples_split=2)
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
acc_min_samples_split_2 = accuracy_score(pred, labels_test)
print "acc_min_samples_split_2",acc_min_samples_split_2

    
def submitAccuracies():
  return {"acc":round(acc,3)}

