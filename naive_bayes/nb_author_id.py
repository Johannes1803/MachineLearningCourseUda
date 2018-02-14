#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import os

##os.chdir("/home/johannes/PycharmProjects/UdacityMLIntro/BayesAnaConda")
import sys
from time import time

print(os.getcwd()+" hurray")
sys.path.append("/home/johannes/PycharmProjects/UdacityMLIntro/BayesAnaConda/tools/")
from email_preprocess import preprocess

from sklearn.naive_bayes import GaussianNB


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

clf = GaussianNB()

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"


GaussianNB(priors=None)

t1 = time()
accuracy = clf.score(features_test, labels_test)
print "comparing time:", round(time()-t1, 3), "s"


print("accuracy: ")
print(accuracy)

#########################################################
### your code goes here ###


#########################################################


