import sympy
from sympy import *
import math
from math import pi, sqrt ,pow

pdf=[]
i=0
l=int(input("\n enter the value of azimutal quantum number:"))
m=int(input("\n enter the value of magnetic quantum number:"))
n=int(input("\n enter the value of principal quantum number:"))
xin=int(input("\n enter the value of x:"))
yin=int(input("\n enter the value of y:"))
zin=int(input("\n enter the value of z:"))
a=int(input("\n enter the value of parameter a:"))
for x in range(-xin,xin+1):
 for y in range(-yin,yin+1):
   for z in range(-zin,zin+1):
        if x!=0 and y!=0 and z!=0 : 
           theta=Symbol('theta')
           fn1=sin(theta)**(2*l)
           der1=diff(fn1,theta,m+l)
           r1=sqrt(x**2+y**2+z**2)
           var1=der1.evalf(subs={theta:math.acos(x/r1)})
           Y=var1*pow(-1,(m+l))*pow(math.sin(x/r1),m)/((2**l)*(math.factorial(l)))*sqrt((2*l+1)/(4*pi)*((math.factorial(l+m))/math.factorial(l-m)))
           r=Symbol('r')
           fn2=exp(-r)*(r**(n+l))
           der2=diff(fn2,r,n+l)
           r2=sqrt(x**2+y**2+z**2)
           fn3=der2*exp(r)
           der3=diff(fn3,r,(2*l+1))
           var3=der3.evalf(subs={r:r2})
           L=(2/(n*a)*pow(-1,(2*l+1))*var3)
           pd=math.exp(-2*r1/(n*a))*pow((2*r1/(n*a)),(2*l))*pow(L,2)*pow(Y,2)*(pow((2/(n*a)),3)*(math.factorial(n-l-1)/(2*n*(pow(math.factorial(n+l),3)))))
           pdf.append(pd)

pdf.sort()
print(pdf)           
print(len(pdf))




        