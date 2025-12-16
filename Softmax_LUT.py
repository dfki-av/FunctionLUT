#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Given: 
#	f(x1 | (x1, x2, x3, x4)) = e^x1 / (e^x1 + e^x2 + e^x3 + e^x4)
# Required:
#	Calculation of f(x1 | (x1, x2, x3, x4))
#-----------------------------------
import numpy as np
import math

def f_x1(x1,x2,x3,x4):
    return math.e**x1/(math.e**x1 + math.e**x2 + math.e**x3 + math.e**x4)
def f_exp(x):
    return math.e**x
def f_inv(x):
    return 1/x

# Initialize
xmin = -5                # lower bound
xmax = +5                # upper bound 
S = 128                  # number of samples
dx = (xmax - xmin)/S     # step size

# Build up the look-up tables using the original functions
exp = [f_exp(x) for x in np.arange(xmin,xmax,dx)]
inv = [f_inv(x) for x in np.arange(xmin,xmax,dx)]

# look-up example
x1 = -0.55
x2 = -1
x3 = 0.5
x4 = 0.87

summation = sum([exp[int((xi-xmin)//dx)] for xi in [x1, x2, x3, x4]])
inv_sum = inv[int((summation-xmin)//dx)]
y = exp[int((x1-xmin)//dx)] * inv_sum

print("Look-up Value: ", y) # >> 0.11050558524263025
print("Function Value : ", f_x1(x1,x2,x3,x4)) # >> 0.11584264325120966
