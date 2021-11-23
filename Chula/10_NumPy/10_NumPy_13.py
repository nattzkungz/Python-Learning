import numpy as np

def p(x):
    logit = -3.98+(0.1*x[:,0])+(0.5*x[:,1])
    prob = 1/(1 + np.e**-logit)
    return prob

exec(input().strip())