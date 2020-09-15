#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    * Network to decode a single digit of the Barcode
    * How does the training size effect the convergence

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

y_test = np.arange(10)
X_test = np.array( [ DigitEncoders[Enc][i] for i in y_test] )
# %%

y = np.random.randint(0,10,1000 )
X = np.array( [ DigitEncoders[Enc][i] for i in y] )

def trainUsingBatchSize(B):
    return MLPClassifier( random_state=1,hidden_layer_sizes=(),max_iter=10000,batch_size=B).fit(X,y)
BatchSizes = [1,10,25,50,100,200]

Cs = [trainUsingBatchSize(B) for B in BatchSizes]
# %%

for C in Cs:
    plt.plot(C.loss_curve_)
plt.legend(BatchSizes)
plt.xlabel('Iterations')
plt.ylabel('Log Loss')
plt.grid()
# %%

for C,B in zip(Cs,BatchSizes):
    y = C.loss_curve_
    x = np.arange(0,len(y))
    plt.plot(x/B,y)
plt.legend(BatchSizes)
plt.xlabel('Iterations')
plt.ylabel('Log Loss')
plt.xlim([0,10])
plt.grid()
# %%

n_iter = np.array( [C.n_iter_ for C in Cs] )
plt.plot(BatchSizes,n_iter,marker='s')
plt.xlabel('Batch size')
plt.ylabel('N iter')
plt.grid()
# %%

for C in Cs:
    plt.plot(C.loss_curve_)
plt.legend(BatchSizes)
plt.xlabel('Iterations')
plt.ylabel('Log Loss')
plt.grid()
# %%

def trainUsingNSamples(Nsamples):
    y = np.random.randint(0,10,Nsamples )
    X = np.array( [ DigitEncoders[Enc][i] for i in y] )
    return MLPClassifier( random_state=1,hidden_layer_sizes=(),max_iter=10000,batch_size=50).fit(X,y) 

Nsamples = np.arange(1000,10000,1000)
Cs = [trainUsingNSamples(Nsample) for Nsample in Nsamples]
# %%

n_iter = np.array( [C.n_iter_ for C in Cs] )
plt.plot(Nsamples,n_iter,marker='s')
plt.xlabel('Sample size')
plt.ylabel('N iter')
plt.grid()
# %%

for C in Cs:
    plt.plot(C.loss_curve_)
plt.legend(Nsamples)
plt.xlabel('Iterations')
plt.ylabel('Log Loss')
plt.grid()
# %%

Nsamples = 1000
y = np.random.randint(0,10,Nsamples )
X = np.array( [ DigitEncoders[Enc][i] for i in y] )
C = MLPClassifier( random_state=1,hidden_layer_sizes=(),max_iter=10000,verbose=1).fit(X,y) 

np.mean( -np.log(np.max( C.predict_proba(X) ,axis=1)) )
#n_iter = np.array( [C.n_iter_ for C in Cs] )
#plt.plot(Nsamples,n_iter)