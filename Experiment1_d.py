#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:50:34 2020

@author: jack
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    * Network to decode a single digit of the Barcode
    * How is the 
    * We aren't applying any noise at the moment so we can make a training set that is just the numbers 0-9
"""
import numpy as np

from sklearn.neural_network import MLPClassifier,MLPRegressor
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from scipy.special import softmax

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
# %%

classifier = MLPClassifier(random_state=1,hidden_layer_sizes=(),max_iter=500,batch_size=1).fit(X,y)
# %%

W = np.matrix( classifier.coefs_[0] )
c = np.matrix( classifier.intercepts_[0] )


i1 = plt.matshow(W,cmap=plt.get_cmap('seismic'))
plt.colorbar(i1)
plt.yticks(range(6))
plt.xticks(range(10))
plt.xlabel('Output class')
plt.ylabel('Input Bit')

i1 = plt.matshow(np.atleast_2d(c),cmap=plt.get_cmap('seismic'))
plt.colorbar(i1)
plt.yticks([])
plt.xticks(range(10))
plt.xlabel('Output class')
# %%

classifier.predict_proba(np.atleast_2d(X_test[0]))
softmax( X_test[0,:].T*W + c)
# %%

plt.matshow(X_test.T)
plt.yticks(range(6))
plt.xticks(range(10))
plt.xlabel('Output class')
plt.ylabel('Input Bit')

# %%

np.multiply( X_test[0,:],W[:,0].T)