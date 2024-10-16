#An Algorithm to Unbias A Clipped Signal

import numpy as np


stds = np.logspace(start=-3,stop=np.log(5),num=100)
thresholds = stds


#do windowing



#If sample within window crosses threshold, do unbiasing.`

from scipy.optimize import fsolve
from scipy.integrate import quad
from scipy.stats import norm

true_mean=
std= 
#generate samples
N #number of samples
samples = 
xbarbiased = samples[samples<tol]
fsolve(lambda xbarhat: xbarbiased*F+(1.-F)*quad(lambda x: norm.pdf(x,xbarhat,sigma)*x,tol,10)/(1-norm.cdf(tol,xbarhat,sigma)) - xbarhat, xbarbiased)
