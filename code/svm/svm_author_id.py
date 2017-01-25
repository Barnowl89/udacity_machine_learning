#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("/Users/Barney/PycharmProjects/machine_learning/code/tools/")
from email_preprocess import preprocess

from sklearn import svm
from sklearn.metrics import accuracy_score
from collections import Counter

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# smaller training dataset
# features_train = features_train[:len(features_train)//100]
# labels_train = labels_train[:len(labels_train)//100]

# for c in [10.0, 100.0, 1000.0, 10000.0, 100000.0]:  # C parameter optimiser

c = 10000

clf = svm.SVC(kernel="rbf", C=c)
t0 = time()
fit = clf.fit(features_train, labels_train)
print("\ntraining time:", round(time()-t0, 3), "s")

t1 = time()
pred = clf.predict(features_test)
print("prediction time:", round(time()-t1, 3), "s")
accuracy = accuracy_score(pred, labels_test)

print(accuracy)

#count the number of emails from Chris (id=1) and Sara (id=0)
print(Counter(pred))

#result for the 20th email
pred[20]