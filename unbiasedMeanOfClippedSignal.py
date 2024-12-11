#An Algorithm to Unbias A Clipped Signal

import numpy as np


stds = np.logspace(start=-3,stop=np.log(5),num=100)
thresholds = stds


#do windowing



#If sample within window crosses threshold, do unbiasing.`

from scipy.optimize import fsolve
from scipy.integrate import quad
from scipy.stats import norm

true_mean=5.
std= 3.
tol=8.
#generate samples
N=1000 #number of samples
samples = np.random.normal(loc=true_mean,scale=std,size=N)
inds_measured = np.where(samples<tol)[0]
inds_notmeasured = np.where(samples>=tol)[0]
xbarbiased = np.mean(samples[inds_measured])
F = np.sum(samples<tol)/N
out = fsolve(lambda xbarhat: xbarbiased*F+(1.-F)*quad(lambda x: norm.pdf(x,xbarhat,std)*x,tol,100)[0]/(1.-norm.cdf(tol,xbarhat,std)[0]) - xbarhat, xbarbiased)[0]

print(out)



import matplotlib.pyplot as plt

plt.figure()
plt.scatter(inds_notmeasured,samples[inds_notmeasured],color='r',s=1,alpha=0.5)
plt.scatter(inds_measured,samples[inds_measured],color='b',s=1,alpha=0.5)
plt.hlines(tol,0,N,color='r',label='Tolerance')
plt.hlines(xbarbiased,0,N,color='b',label=r'$\bar{x}_{biased}$')
plt.hlines(true_mean,0,N,color='k',label=r'$\bar{x}$')
plt.hlines(out,0,N,color='k',linestyle='--',label=r'$\hat{\bar{x}}$')
plt.legend()
plt.xlabel('Samples')
plt.ylabel('Values')
plt.show(block=False)

