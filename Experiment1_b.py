#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    * Network to decode a single digit of the Barcode
    * What can 
    * We aren't applying any noise at the moment so we can make a training set that is just the numbers 0-9
"""
import numpy as np

from sklearn.neural_network import MLPClassifier,MLPRegressor
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

from sklearn.preprocessing import MultiLabelBinarizer,LabelBinarizer

import category_encoders as ce
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

C0 = MLPClassifier( random_state=1,hidden_layer_sizes=(),max_iter=10000).fit(X,y)
# %%

#encoder =  LabelBinarizer()
encoder = ce.binary.BinaryEncoder(verbose=1,return_df = False)
encoder.fit(y)
y_enc = encoder.transform(y_test)

print(y_enc)