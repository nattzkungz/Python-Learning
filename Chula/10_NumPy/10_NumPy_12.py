import numpy as np

def toCelsius(f):
    return (f - 32) *(5/9)

def BMI(wh):
    return wh[:,0]/(wh[:,1]/100)**2

def distanceTo(p, Points):
    return np.sqrt(((Points[:,0]-p[0])**2) + ((Points[:,1] - p[1])**2))

exec(input().strip())
