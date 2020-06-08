# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 19:42:48 2020

@author: lucas
"""

import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

##############################################################
import warnings
warnings.filterwarnings("ignore") #pour ignorer les warning dans la console
##############################################################

df = pd.read_csv("KDD_attack_name_change.csv")


X = df.drop('attack_name', axis = 1)
Y = df['attack_name']

mlp = MLPClassifier(hidden_layer_sizes = (64,32,16), random_state = 1)
dt = DecisionTreeClassifier(min_samples_leaf = 0.15, random_state = 1)

classifiers = [('DecisionTreeClassifier',dt), ('MLPClassifier', mlp)]

for clf_name, clf in classifiers:
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 20)
    
    clf.fit(X_train, Y_train)
    clf_predict = clf.predict(X_test)
    clf_accuracy_score = accuracy_score(Y_test, clf_predict)
    
    print(clf_name, " accuracy score : ",clf_accuracy_score)



