import numpy as np
import matplotlib.pyplot as plt
import math
import random
import plotly.express as px


ay=[]
by=[]
cy=[]
nx=[]
ny=[]
nz=[]
orbital =''

def probdensity(r,orbital,x,y,z):
    density=0

    if orbital == '1s':
        density= (math.exp(-2 * r))*5000
    elif orbital == '2s':
        density= (math.exp(-r)*(pow(-r+2,2)))*1000
    elif orbital == '3p':
        density= (math.exp(-2*r/3)*((-r**2+4*r)**2))*(x**2/(x**2+y**2))*50
    elif orbital == '4p':
        density= 5*((math.exp(-r/2)*(r**2)*((15*(r**2)-300*r+1200)**2))*(x**2/(x**2+y**2)))/5000
    elif orbital == '4s':
        density = 9*math.pow(((-r**3/2 + 12*r**2 - 72*r + 96)*(1/(2*math.sqrt(math.pi)))*math.exp(-r/4)),2)
    elif orbital == '2p':
        density = 49*math.pow(r*math.exp(-r/2)*6*(math.sqrt(3/4*(math.pi)))*z/r,2)
    elif orbital == '3s':
        density =320*math.pow((math.exp(-r/3)*(4/3*r**2-12*r+18))*1/(2*math.sqrt(math.pi)),2)
    elif orbital == '3d':
        density = (1/100)*math.pow(math.exp(-r/3)*math.pow(2*r/3,2)*120*math.sqrt(5/(16*math.pi))*(3*math.pow(z/r,2)-1),2)
    elif orbital == '4d':
        density =1/500 * math.pow((-1440*(r/4 - 3))*math.exp(-r/2)*math.pow(r/2,2)*math.sqrt(5/(16*math.pi))*(3*math.pow(z/r,2)-1),2)
    elif orbital == '4f':
        density =1/27000*math.pow( 5040*math.exp(-r/2)*math.pow(r/2,3)*math.sqrt(7/(16*math.pi))*(5*math.pow(z/r,3)-3*z/r),2)

    if not math.isnan(density):
        return density
    else :
        return 0

def random_points_sphere(x,y,z,k,step):
    for i in range(math.floor(k)):
        theta = random.random() * 2 * math.pi
        v = random.random()
        phi = math.acos((2 * v) - 1)
        r = math.pow(random.random(), 1 / 3) * step
        xp = r * math.sin(phi) * math.cos(theta) + x
        yp = r * math.sin(phi) * math.sin(theta) + y
        zp = r * math.cos(phi) + z
        ay.append(xp)
        by.append(yp)
        cy.append(zp)


def sphere(k):
 ay = []
 by = []
 cy = []

 R = 40
 n = 10000



 for i in range(0, n):
    phi = random.random() *2*math.pi
    costheta = random.random()*random.randrange(-1,2)
    u = random.random()
    theta = math.acos(costheta)
    r = R * math.pow(u, 1/3)
    x = (r * math.sin(theta) * math.cos(phi))

    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(theta)
    step = 2
    if int(math.floor(k)) > 0:
        for i in range((math.floor(k))):
            ay.append((x - 2) + (random.random() * (step)))
            by.append((y - 2) + (random.random()  * (step)))
            cy.append((z - 2) + (random.random()  * (step)))

def randomplot():
    plt.rcParams['figure.figsize']=(6,4)
    plt.rcParams['figure.dpi']=150
    plt.rcParams["scatter.edgecolors"]='none'


    print('enter the orbit')
    orbital=input()      #the orbital of user choice has taken as input
    #print(orbital)

    for x in np.arange(-60.0,60.0,4):  #np.arange is used when step size is a floating point
        for y in np.arange(-60,60.0,4):
            for z in np.arange(-60.0,60.0,4):

                r=math.sqrt((x**2+y**2+z**2)) #radial distance is calculated

                k = probdensity(r,orbital,x,y,z) #probability density psi is calculated in a seperate function
                print(k)

                random_points_sphere(x, y, z, k,4)


    fig=px.scatter_3d(x=ay,y=by,z=cy,title=orbital+' orbital',height=960,width=960,template='plotly_dark',)
    fig.update_traces(marker_size=1,)
    fig.update_traces(marker_color='teal')
    #fig.show()

    fig.write_html("index.html")

    print('done')
