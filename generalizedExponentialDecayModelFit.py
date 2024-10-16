import numpy as np

def expFunc(x,a,b,c):
    """
    Of the form y(x)=a+b*e^(c*x)
    Args:
        x
        a
        b
        c
    Returns:
        y
    """
    return a+b*np.exp(c*x)

def generalizedExponentialDecayModelFit(x,y):
    """
    https://stackoverflow.com/questions/3938042/fitting-exponential-decay-with-no-initial-guessing
    Args:
        x - x points
        y - y points
    Returns:
        a
        b
        c
    """
    n = len(x)
    s = np.zeros(n)
    for i in np.arange(1,n):
        s[i] = s[i-1] + 0.5*(y[i]+y[i-1])*(x[i]-x[i-1])

    a0 = np.sum([(x[i]-x[0])**2. for i in np.arange(n)])
    a1 = np.sum([(x[i]-x[0])*s[i] for i in np.arange(n)])
    a2 = a1
    a3 = np.sum([s[i]**2. for i in np.arange(n)])
    b0 = np.sum([(x[i]-x[0])*(y[i]-y[0]) for i in np.arange(n)])
    b1 = np.sum([(y[i]-y[0])*s[i] for i in np.arange(n)])
    c = a0*b1/(a0*a3 - a1*a2) - a2*b0/(a0*a3 - a1*a2)    

    c0 = n
    c1 = np.sum([np.exp(c*x[i]) for i in np.arange(n)])
    c2 = c1
    c3 = np.sum([np.exp(2.*c*x[i]) for i in np.arange(n)])
    d0 = np.sum([y[i] for i in np.arange(n)])
    d1 = np.sum([y[i]*np.exp(c*x[i]) for i in np.arange(n)])

    a = -c1*d1/(c0*c3 - c1*c2) + c3*d0/(c0*c3 - c1*c2)
    b = c0*d1/(c0*c3 - c1*c2) - c2*d0/(c0*c3 - c1*c2)
    
    return a,b,c

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    xs = np.linspace(-2,4,num=100)
    a,b,c = (1,1,1)
    ys = expFunc(xs,a,b,c)
    ys = ys + np.random.normal(loc=0.,scale=0.1,size=100)

    a,b,c = generalizedExponentialDecayModelFit(xs,ys)
    ys_fit = expFunc(xs,a,b,c)

    plt.figure()
    plt.scatter(xs,ys,color='k')
    plt.plot(xs,ys_fit,color='blue')
    plt.show(block=False)







