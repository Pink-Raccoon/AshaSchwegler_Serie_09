# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 22:23:05 2021

@author: Asha
"""

import numpy as np
from AshaSchwegler_S9_Aufg2 import AshaSchwegler_S9_Aufg2

def AshaSchwegler_S9_Aufg3():
    for i in range(1000):
        A = np.random.rand(100,100)
        b = np.random.rand(100,1)
        squiggle_A = A + np.rand(100,100)/10^5
        squiggle_b = b + np.rand(100,1)/10^5
        d_max = AshaSchwegler_S9_Aufg2(A, squiggle_A, b, squiggle_b).d_max
        d_obs = AshaSchwegler_S9_Aufg2(A, squiggle_A, b, squiggle_b).d_max.d_obs
        verh = d_max/d_obs
        return d_max, d_obs, verh
        
