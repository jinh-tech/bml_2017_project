#!/usr/bin/python

import numpy as np
from os import listdir
from os.path import isfile, join
import os.path
import random

def movielens(binary,threshold):
    file_path = 'data/X.txt'
    X = np.loadtxt(file_path)
    if binary == False:
        return X
    
    for i in range(0,X.shape[0]):
        for j in range(0,X.shape[1]):
            if X[i][j]<=threshold:
                X[i][j] = 0
            else:
                X[i][j] = 1
                
    return X