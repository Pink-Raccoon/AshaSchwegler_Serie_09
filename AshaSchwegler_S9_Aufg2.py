# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 21:12:00 2021

@author: Asha
"""

import numpy as np

def AshaSchwegler_S9_Aufg2(A,squiggle_A,b,squiggle_b): 
   cond_A = np.linalg.cond(A,np.inf)
   squiggle_A_inf = np.linalg.norm((A+squiggle_A),np.inf)
   A_inf = np.linalg.norm(A,np.inf)
   squiggle_b_inf = np.linalg.norm((b+squiggle_b),np.inf)
   b_inf = np.linalg.norm(b,np.inf) 
   if checkCond(A, squiggle_A) == True:
      d_max = ((cond_A/(1-(cond_A*squiggle_A_inf/A_inf)))*((squiggle_A_inf/A_inf)+(squiggle_b_inf/b_inf)))
      result_ohneFehler = np.linalg.solve(A,b)
      result_mitFehler = np.linalg.solve((A+squiggle_A),(b+squiggle_b))
      d_obs = result_ohneFehler - result_mitFehler
      return d_max, d_obs
   else: 
      return "NaN"
        
        
    
    
def checkCond(A, squiggle_A):
    cond_A = np.linalg.cond(A,np.inf)
    squiggle_A_inf = np.linalg.norm((A+squiggle_A),np.inf)
    A_inf = np.linalg.norm(A,np.inf)
    if cond_A * ((squiggle_A_inf)/A_inf):
        return True
    else: return False
    
    
A = np.array([[20,30,10],[10,17,6],[2,3,2]])
b = np.array([[5200],[3000],[760]])
squiggle_A = 0.1
squiggle_b = 100



print(AshaSchwegler_S9_Aufg2(A,squiggle_A,b,squiggle_b))


