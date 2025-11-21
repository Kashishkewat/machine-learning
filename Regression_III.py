import numpy as np   # random number generator
import pandas as pd
import matplotlib.pyplot as plt  # graphing functionality
import statsmodels.formula.api as smf 

# Create two lists with random data and a designed linear dependency between the lists. Put the data into a DataFrame.
X_var = []
Y_var = []

for k in range (1, 100):
    x = k + 15
    X_var.append(x + np.random.normal(loc=0.0, scale=4.0))
    Y_var.append(x*1.5 + np.random.normal(loc=0.0, scale=6.0))
    
Regr_data = pd.DataFrame(list(zip(X_var, Y_var)), columns=['X', 'Y'])