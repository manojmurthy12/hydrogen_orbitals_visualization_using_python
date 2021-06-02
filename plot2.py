import numpy as np
import math
from random_geometry_points.sphere import Sphere
import pandas as pd  # (version 1.0.0)
import plotly.express as px  # (version 4.7.0)
import plotly.io as pio
import plotly.graph_objects as go
import probdensity_structured
ay=[]
by=[]
cy=[]
nx=[]
ny=[]
nz=[]
orbital =''
# Use for animation rotation at the end
x_eye = -1.25
y_eye = 2
z_eye = 0.5

import sympy
from sympy import *
import math
from math import pi, sqrt ,pow

def probability_density(n,l,m,x,y,z,a):
    theta = Symbol('theta')
    fn1 = sin(theta) ** (2 * l)
    der1 = diff(fn1, theta, m + l)
    r1 = sqrt(x ** 2 + y ** 2 + z ** 2)
    var1 = der1.evalf(subs={theta: math.acos(x / r1)})
    Y = var1 * pow(-1, (m + l)) * pow(math.sin(x / r1), m) / ((2 ** l) * (math.factorial(l))) * sqrt(
        (2 * l + 1) / (4 * pi) * ((math.factorial(l + m)) / math.factorial(l - m)))
    r = Symbol('r')
    fn2 = exp(-r) * (r ** (n + l))
    der2 = diff(fn2, r, n + l)
    r2 = sqrt(x ** 2 + y ** 2 + z ** 2)
    fn3 = der2 * exp(r)
    der3 = diff(fn3, r, (2 * l + 1))
    var3 = der3.evalf(subs={r: r2})
    L = (2 / (n * a) * pow(-1, (2 * l + 1)) * var3)
    pd = math.exp(-2 * r1 / (n * a)) * pow((2 * r1 / (n * a)), (2 * l)) * pow(L, 2) * pow(Y, 2) * (
                pow((2 / (n * a)), 3) * (math.factorial(n - l - 1) / (2 * n * (pow(math.factorial(n + l), 3)))))
    if not math.isnan(pd):
        return pd
    else:
        return 0


def probdensity2(r, orbital, x, y):
    density=0
    if orbital == '1s':
        density= (math.exp(-2 * r))*5000
    elif orbital == '2s':
        density= (math.exp(-r)*(pow(-r+2,2)))*500
    elif orbital == '3p':
        density= (math.exp(-2*r/3)*((-r**2+4*r)**2))*(x**2/(x**2+y**2))*10
    elif orbital == '4p':
        density= ((math.exp(-r/2)*(r**2)*((15*(r**2)-300*r+1200)**2))*(x**2/(x**2+y**2)))/5000

    if not math.isnan(density):
        return density
    else :
        return 0


def randomsphere2(x, y, z, k):   #this function is used to generate random points with the centre being the point where
    #probability density k is found
    sphere = Sphere(x, y, z, 10)
    #print(k)
    if int(math.floor(k)) > 0:  #math.floor is done to make the number an integer
        random_sphere_points = sphere.create_random_points(int(math.floor(k)))
        for i in range(len(random_sphere_points)):
            ay.append(random_sphere_points[i][0])
            by.append(random_sphere_points[i][1])
            cy.append(random_sphere_points[i][2])


def randomplot2():
    #print('enter the orbit')
    #orbital=input()      #the orbital of user choice has taken as input
    #print(orbital)

    for x in np.arange(-40.0,40.0,10.0):  #np.arange is used when step size is a floating point
        for y in np.arange(-40.0,40.0,10.0):
            for z in np.arange(-40.0,40.0,10.0):

                #r=math.sqrt((x**2+y**2+z**2)) #radial distance is calculated

                k =100000*probability_density(7,4,0,x,y,z,40/49)#probability density psi is calculated in a seperate function
                print(k)

                randomsphere2(x, y, z, k) #random points are generated around the point (x,y,z) to plot


    #nucleus = Sphere(0, 0, 0, 0.00001*(max(ay)+max(by)+max(cy))/3) #radius of nucleus is found here(it applies only for 1s orbital
    #nucleus_points = nucleus.create_random_points(1000)
    # for t in range(len(nucleus_points)):
    #     nx.append(nucleus_points[t][0])
    #     ny.append(nucleus_points[t][1])
    #     nz.append(nucleus_points[t][2])


    fig=px.scatter_3d(x=ay,y=by,z=cy,title=orbital+' orbital',height=700)
    fig.update_traces(marker_size=2)

    # fig.update_layout(scene_camera_eye=dict(x=x_eye, y=y_eye, z=z_eye),
    #                   updatemenus=[dict(type='buttons',
    #                                     showactive=False,
    #                                     y=1,
    #                                     x=0.8,
    #                                     xanchor='left',
    #                                     yanchor='bottom',
    #                                     pad=dict(t=45, r=10),
    #                                     buttons=[dict(label='Play',
    #                                                   method='animate',
    #                                                   args=[None, dict(frame=dict(duration=250, redraw=True),
    #                                                                    transition=dict(duration=0),
    #                                                                    fromcurrent=True,
    #                                                                    mode='immediate'
    #                                                                    )]
    #                                                   )
    #                                              ]
    #                                     )
    #                                ]
    #                   )
    #
    #
    # def rotate_z(x, y, z, theta):
    #     w = x + 1j * y
    #     return np.real(np.exp(1j * theta) * w), np.imag(np.exp(1j * theta) * w), z
    #
    # frames = []
    #
    # for t in np.arange(0, 6.26, 0.1):
    #     xe, ye, ze = rotate_z(x_eye, y_eye, z_eye, -t)
    #     frames.append(go.Frame(layout=dict(scene_camera_eye=dict(x=xe, y=ye, z=ze))))
    # fig.frames = frames



    fig.write_html("index.html")
    print('done')


