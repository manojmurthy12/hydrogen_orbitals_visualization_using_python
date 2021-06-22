import random
from random import *
import math

import numpy as np
import random
import math
from random_geometry_points.sphere import Sphere
import pandas as pd  # (version 1.0.0)
def sphere(k):
 ay = []
 by = []
 cy = []
 k = []
 R = 40
 n = 10000



 for i in range(0, n):
    phi = random.random() *2*math.pi
    costheta = random.random()*randrange(-1,2)
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



