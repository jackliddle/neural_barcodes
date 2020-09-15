#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 21:50:52 2020

@author: jack
"""
import numpy as np

from sklearn.neural_network import MLPClassifier,MLPRegressor
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from scipy.special import softmax
from collections import defaultdict
import matplotlib.pyplot as plt
# %%

import pprint
pp = pprint.PrettyPrinter(indent=4)
# %%

from Encoders import DigitEncoders
# %%

Enc = 'L'

y = np.random.randint(0,10,10000)
X = np.array( [ DigitEncoders[Enc][i] for i in y] )
X_wnoise = X + np.random.normal(0,0.1,X.shape)
# %%

X_train, X_test, y_train, y_test = train_test_split(X_wnoise, y, test_size=0.33, random_state=42)
classifier = MLPClassifier(random_state=1,hidden_layer_sizes=(),max_iter=500,batch_size=10).fit(X_train,y_train)
# %% How many errors and in which digits

y_pred = classifier.predict(X_test)
Errors = defaultdict(list)
for yp,yt in zip(y_pred,y_test):
    if yp != yt:
        Errors[yt].append(yp)
        
pp.pprint(Errors)