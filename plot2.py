import numpy as np
import random
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
a=0.529*pow(10,-10)

#n=5
#step=1
n_orbital=4
l_azimuthal=2
m_magnetic=1

import sympy
from sympy import *
import math
from math import pi, sqrt ,pow

def probability_density(n,l,m,x,y,z,a,step):
    #print(pi)
    theta = Symbol('theta')
    fn1 = sin(theta)**(2 * l)
    der1 = diff(fn1, theta, m + l)
    r1 = sqrt(x ** 2 + y ** 2 + z ** 2)
    #pi=math.pi
    thetacons= z / r1
    var1 = der1.evalf(subs={theta: math.acos(thetacons)})
    Y = var1 * pow(-1, (m + l)) * pow(math.sin(thetacons), m) / ((2 ** l) * (math.factorial(l))) * sqrt(
        (2 * l + 1) / (4 * pi) * ((math.factorial(l + m)) / math.factorial(l - m)))
    r = Symbol('r')
    fn2 = exp(-r) * (r**(n + l))
    der2 = diff(fn2, r, n + l)
    r2 = sqrt(x ** 2 + y ** 2 + z ** 2)
    fn3 = der2 * exp(r)
    der3 = diff(fn3, r, (2 * l + 1))
    var3 = der3.evalf(subs={r: r2})
    L = (2 / (n * a) * pow(-1, (2 * l + 1)) * var3)
    pd =pow(10,-17)*pow(step,3)*math.exp(-2 * r1 / (n * a)) * pow((2 * r1 / (n * a)), (2 * l)) * pow(L, 2) * pow(Y, 2)*(pow((2/(n*a)), 3)*(math.factorial(n-l-1)/(2*n*(pow(math.factorial(n+l), 3)))))
    i=1
    if not math.isnan(pd):
        return pd
    else:
        return 0



def randomsphere2(x, y, z, k,step):   #this function is used to generate random points with the centre being the point where
    #probability density k is found
    sphere = Sphere(x, y, z, step)
    #print(k)
    if int(math.floor(k)) > 0:  #math.floor is done to make the number an integer
        random_sphere_points = sphere.create_random_points(int(math.floor(k)))
        for i in range(len(random_sphere_points)):
            ay.append(random_sphere_points[i][0])
            by.append(random_sphere_points[i][1])
            cy.append(random_sphere_points[i][2])

def random_points_square(x,y,z,k,step):
    if int(math.floor(k)) > 0:
        for i in range((math.floor(k))):
            ay.append((x - step / 2) + (random.random() * (step)))
            by.append((y - step / 2) + (random.random()  * (step)))
            cy.append((z - step / 2) + (random.random()  * (step)))
def random_points_sphere(x,y,z,k,step):
    radius=math.sqrt(x**2 + y**2 + z**2)
    if int(math.floor(k)) > 0:
        for i in range((math.floor(k))):
            ay.append((x - step) + (random.random() * (step)))
            by.append((y - step) + (random.random()  * (step)))
            cy.append((z - step) + (random.random()  * (step)))


def randomplot2():
    #print('enter the orbit')
    #orbital=input()      #the orbital of user choice has taken as input

    step = (2*(n_orbital ** 2) * a) / 5
    for x in np.arange(-2*(n_orbital**2)*a, 2*(n_orbital**2)*a, step):  #np.arange is used when step size is a floating point
        for y in np.arange(-2*(n_orbital**2)*a, 2*(n_orbital**2)*a, step):
            for z in np.arange(-2*(n_orbital**2)*a, 2*(n_orbital**2)*a, step):

                #r=math.sqrt((x**2+y**2+z**2)) #radial distance is calculated

                k=probability_density(n_orbital,l_azimuthal,m_magnetic,x,y,z,a,step)#probability density psi is calculated in a seperate function
                print(k)

                if k<200:
                    random_points_square(x,y,z,k,step)
                else:
                    random_points_square(x,y,z,200,step)

            #random points are generated around the point (x,y,z) to plot


    #nucleus = Sphere(0, 0, 0, 0.00001*(max(ay)+max(by)+max(cy))/3) #radius of nucleus is found here(it applies only for 1s orbital
    #nucleus_points = nucleus.create_random_points(1000)
    # for t in range(len(nucleus_points)):
    #     nx.append(nucleus_points[t][0])
    #     ny.append(nucleus_points[t][1])
    #     nz.append(nucleus_points[t][2])


    fig=px.scatter_3d(x=ay,y=by,z=cy,title=orbital+' orbital',height=700)
    fig.update_traces(marker_size=1)

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


