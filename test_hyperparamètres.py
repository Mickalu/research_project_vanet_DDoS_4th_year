# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 19:42:48 2020

@author: lucas
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import plot_confusion_matrix


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error as MSE

from sklearn.metrics import classification_report, confusion_matrix


##############################################################
import warnings
warnings.filterwarnings("ignore") #pour ignorer les warning dans la console
##############################################################

df = pd.read_csv("KDD_clean_database.csv")

X = df.drop('attack_name', axis = 1)
y = df['attack_name']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 10, stop = 200, num = 25)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt', 'log2']
# Maximum number of levels in tree
max_depth = [x for x in range(1, 100, 1)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]

criterion = ['gini', 'entropy']
# Create the random grid
random_grid = {'max_depth': max_depth}

# Use the random grid to search for best hyperparameters
# First create the base model to tune
rf = RandomForestClassifier(random_state=1)
# Random search of parameters, using 3 fold cross validation, 
# search across 100 different combinations, and use all available cores
rf_random = GridSearchCV(rf, random_grid, cv = 5)
# Fit the random search model
rf_random.fit(X, y)

print(rf_random.best_params_)

# rf2 = RandomForestClassifier(n_estimators=128, bootstrap=False, random_state=1)
# - n_estimators=128 
# - max_features='auto' (par défaut)
# - bootstrap=False
# - criterion='gini' (par défaut)
# - 

# rf.fit(X_train, y_train)
# rf2.fit(X_train, y_train)

# rf_predict = rf.predict(X_test)
# rf2_predict = rf2.predict(X_test)
   
# rf_accuracy_score = accuracy_score(y_test, rf_predict)
# rf2_accuracy_score = accuracy_score(y_test, rf2_predict) 

# print("rf accuracy_score : ", rf_accuracy_score)   
# print("rf2 accuracy_score : ", rf2_accuracy_score)
# print(rf2_accuracy_score - rf_accuracy_score)