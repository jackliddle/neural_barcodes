#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    * Network to decode a single digit of the Barcode
    * Are we doing regression or classification?
        * How does this play with the random state.

    * We aren't applying any noise at the moment so we can make a training set that is just the numbers 0-9
"""
import numpy as np

from sklearn.neural_network import MLPClassifier,MLPRegressor
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt


# %%

from Encoders import DigitEncoders
# %%
Enc = 'L'
Npow=3
Nsamples = int(pow(10,Npow))

y = np.random.randint(0,10,Nsamples )
X = np.array( [ DigitEncoders[Enc][i] for i in y] )

y_test = np.arange(10)
X_test = np.array( [ DigitEncoders[Enc][i] for i in y_test] )
# %%

random_states = range(20)
Rs = [ MLPRegressor( random_state=random_state,hidden_layer_sizes=(),max_iter=10000).fit(X,y) for random_state in random_states]
Cs = [ MLPClassifier(random_state=random_state,hidden_layer_sizes=(),max_iter=10000).fit(X,y) for random_state in random_states]
# %%

R_pred = [R.predict(X_test) for R in Rs]
C_pred = [C.predict(X_test) for C in Cs]
for R in R_pred:
    print(R)
    
for C in C_pred:
    print(C)