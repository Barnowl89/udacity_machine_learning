#!/usr/bin/python

"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatterplot of the training/testing data

    You fill in the regression code where indicated:
"""    


import sys
import pickle
import os
import numpy as np

sys.path.append("/Users/Barney/PycharmProjects/machine_learning/code/tools/")
from feature_format import featureFormat, targetFeatureSplit
data_path = "/Users/Barney/PycharmProjects/machine_learning/lib/ud120-projects"
tools_path = "/Users/Barney/PycharmProjects/machine_learning/tools"

dictionary = pickle.load(open(os.path.join(data_path, 'final_project', 'final_project_dataset_modified.pkl'), 'br'))
    # "/Users/Barney/PycharmProjects/machine_learning/lib/ud120-projects"
    #                           "/final_project/final_project_dataset_modified.pkl", "br"))

# list the features you want to look at--first item in the
# list will be the "target" feature
features_list = ["bonus", "salary", "long_term_incentive"]
data = featureFormat(dictionary, features_list, remove_any_zeroes=True,
                     sort_keys=os.path.join(data_path, 'tools', 'python2_lesson06_keys.pkl'))
target, features = targetFeatureSplit(data)

# training-testing split needed in regression, just like classification
from sklearn.model_selection import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5,
                                                                          random_state=42)
train_color = "b"
test_color = "r"



### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and 
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.
from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(feature_train, target_train)

print(reg.intercept_, reg.coef_)
print(reg.score(feature_train, target_train))



### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
feat_test = np.array(feature_test)  # tidy. me the features a numpy array
feat_train = np.array(feature_train)  # tidy. me the features a numpy array
feat_test_target = feat_test[:, 0]
feat_train_target = feat_train[:, 0]
for feature, target in zip(feat_test_target, target_test):  # get all of the n subarrays, i.e. the nth feature
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feat_train_target, target_train):
    plt.scatter( feature, target, color=train_color ) 

### labels for the legend
plt.scatter(feat_test_target[0], target_test[0], color=test_color, label="test")
plt.scatter(feat_test_target[0], target_test[0], color=train_color, label="train")




### draw the regression line, once it's coded
try:
    plt.plot( feat_test_target, reg.predict(feat_test_target) )
except NameError:
    pass

reg.fit(feat_test_target, target_test)
plt.plot(feat_train_target, reg.predict(feat_train_target), color="b")
plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()
