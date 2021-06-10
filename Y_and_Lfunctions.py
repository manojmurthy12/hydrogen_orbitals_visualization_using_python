import sympy
from sympy import *
import math
from math import pi, sqrt, pow
a=0.529*pow(10,-10)

n_orbital = 2

def Y_function(n,l,m,x,y,z,a):
    if m >= 0:
        eps = pow(-1, m)
    else:
        eps = 1
    theta = Symbol('theta')

    fn1 = (sin(theta)) ** (2 * l) * (-1) **2* l
    der_fn = diff(fn1, theta, (abs(m) + l))
    der_t = diff(cos(theta), theta)**(abs(m) + l)
    der = der_fn/der_t
    radius = sqrt(x ** 2 + y ** 2 + z ** 2)

    thetacons = z / radius
    value = der.evalf(subs={theta: math.acos(thetacons)})

    Y = value * eps * pow(math.sin(thetacons), abs(m)) / ((2 ** l) * (math.factorial(l))) * sqrt(
        (2 * l + 1) / (4 * pi) * ((math.factorial(l + abs(m)) / math.factorial(l - abs(m)))))
    return Y



def L_function(n,l,m,x,y,z,a):
    r = Symbol('r')

    fn = exp((-2 * r / n * a)) * ((2 * r / n * a) ** (n + l))
    der_fn = diff(fn, r, n + l)
    der_par = diff((2 * r / n * a), r)**(n + l)
    der = der_fn/der_par
    radius = sqrt(x ** 2 + y ** 2 + z ** 2)

    fn3 = der * exp((2 * r / n * a))
    der_fnf = diff(fn3, r, (2 * l + 1))
    der_par2 = diff((2 * r / n * a), r)**(2 * l + 1)
    der2 = der_fnf/der_par2
    value = der2.evalf(subs={r: radius})
    L = pow(-1, (2 * l + 1)) * value
    return L
Y= Y_function(1, 0, 0,0,0,0,a)
L = Y_function(1, 0, 0,-2*(n_orbital**2)*a,+2*(n_orbital**2)*a,+2*(n_orbital**2)*a,a)
print("Y:%d \n L=%d" % (Y, L))
