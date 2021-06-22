import sympy
from sympy import *

r = Symbol('r')
der = diff(exp(-r/2)*(r/2)**7,r,7)
der = der * (2**7) * exp(r/2)
der = -(2**7)*diff(der,r,7)
print(der)