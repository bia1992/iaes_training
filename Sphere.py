# -*- coding: utf-8 -*-
# date: 25/10/13
# username: bia1992
# name: Bannov Il'ya
# description: Sphere with random points
__author__ = 'Bannov Ilya'
__copyright__ = "Copyright 2013, Bannov Ilya"
__credits__ = ["Bannov Ilya"]
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "bannov.ilya@gmail.com"
__status__ = "Development"

import numpy as np
from mayavi import mlab

#Create sphere
r = 0.3
pi = np.pi
cos = np.cos
sin = np.sin
phi, theta = np.mgrid[0:pi:101j, 0:2*pi:101j]

x = r*sin(phi)*cos(theta)
y = r*sin(phi)*sin(theta)
z = r*cos(phi)

sphere = mlab.mesh(x, y, z)
mlab.show()

# Create random points on sphere
i = 0
while i < 50:
    rand1 = np.random.randint(0, len(x) - 1)
    rand2 = np.random.randint(0, len(x) - 1)
    xPoint = x[rand1][rand2]
    yPoint = y[rand1][rand2]
    zPoint = z[rand1][rand2]
    i += 1
    points = mlab.points3d(xPoint, yPoint, zPoint, zPoint, mode='point', colormap="Blues")
    points.actor.property.point_size = 5
    mlab.text3d(xPoint, yPoint, zPoint, 'Point ' + str(i) + ', x=' + str(round(xPoint, 3)) + ' y=' + str(round(yPoint, 3)) + ' z=' + str(round(zPoint, 3)), scale = 0.01)



