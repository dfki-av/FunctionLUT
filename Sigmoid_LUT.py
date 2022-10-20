#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Given: 
#	f(x) = 1 / (1 + e^-x)
# Required:
#	Y: look-up table of f(x)
#-----------------------------------
import numpy as np
import math

def f(x):
    return 1/(1+math.e**-x)

# Initialize
xmin = -5
xmax = +5
S = 256
dx = (xmax - xmin)/S

# Build up the look-up table
Y = [f(x) for x in np.arange(xmin,xmax,dx)]

# look-up example
x = 0.55
idx = int((x - xmin)//dx)
y = Y[idx]
print("Look-up Value: ", y) # >> 0.6334102636778401
print("Function Value : ", f(x)) # >> 0.6341355910108007

# Calculate the error (optional)
error = 0
for x in np.arange(xmin,xmax,dx/100):
    idx = int((x - xmin)//dx)
    error = max(error, abs(f(x)-Y[idx]))

print("Maximum Error = ", error) # >> 0.009764383424879064
