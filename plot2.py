import numpy as np
import math
from random_geometry_points.sphere import Sphere
import pandas as pd  # (version 1.0.0)
import plotly.express as px  # (version 4.7.0)
import plotly.io as pio
import plotly.graph_objects as go

ay=[]
by=[]
cy=[]
nx=[]
ny=[]
nz=[]
orbital =''

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
    sphere = Sphere(x, y, z, 2)
    #print(k)
    if int(math.floor(k)) > 0:  #math.floor is done to make the number an integer
        random_sphere_points = sphere.create_random_points(int(math.floor(k)))
        for i in range(len(random_sphere_points)):
            ay.append(random_sphere_points[i][0])
            by.append(random_sphere_points[i][1])
            cy.append(random_sphere_points[i][2])


def randomplot2():
    print('enter the orbit')
    orbital=input()      #the orbital of user choice has taken as input
    #print(orbital)

    for x in np.arange(-40.0,40.0,2):  #np.arange is used when step size is a floating point
        for y in np.arange(-40,40.0,2):
            for z in np.arange(-40.0,40.0,2):

                r=math.sqrt((x**2+y**2+z**2)) #radial distance is calculated

                k = probdensity2(r, orbital, x, y) #probability density psi is calculated in a seperate function
                #print(k)

                randomsphere2(x, y, z, k) #random points are generated around the point (x,y,z) to plot


    nucleus = Sphere(0, 0, 0, 0.00001*(max(ay)+max(by)+max(cy))/3) #radius of nucleus is found here(it applies only for 1s orbital
    nucleus_points = nucleus.create_random_points(1000)
    for t in range(len(nucleus_points)):
        nx.append(nucleus_points[t][0])
        ny.append(nucleus_points[t][1])
        nz.append(nucleus_points[t][2])


    fig=px.scatter_3d(x=ay,y=by,z=cy,title=orbital+' orbital',height=700)
    fig.update_traces(marker_size=2)
    fig.show()


