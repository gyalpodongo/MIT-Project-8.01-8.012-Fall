# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:44:10 2020

@author: Gyalpo
"""

#Need to create function for Center of Mass

from vpython import*
import numpy as np
import math

scene.forward = vector(1,-3,-1)

G = 6.7e-11
vector_momentum = vector(0,0,-1e-2)

class Coordinate(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def distance(self,other):
        d_x = self.x - other.x
        d_y = self.y - other.y
        d_z = self.z - other.z
        d = (d_x**2 + d_y**2 + d_z**2)**0.5
        return d
    
#class body(sphere):
    #def __init__(self,position,radius,mass,color,make_trail = True,interval = 10, retain = 50):
        #sphere.__init__(self,mass)
        #self.mass = mass
        #self.momentum = mass*vector_momentum
            
            
        
    
    
def center_mass(planet1,planet2) :
    cm_x = (mass1*coordinate1.x + mass2*coordinate2.x)/(mass1+mass2)
    cm_y = (mass1*coordinate1.y + mass2*coordinate2.y)/(mass1+mass2)
    cm_z = (mass1*coordinate1.z + mass2*coordinate2.z)/(mass1+mass2)
    cm = vector(cm_x,cm_y,cm_z)
    return cm

sun = sphere(pos= vector(-1e11,0,0),radius= 9e9,color = color.yellow,make_trail = True,interval = 10, retain = 50)
earth = sphere(pos= vector(1.5e11,0,0),radius= 9e9,color =color.cyan,make_trail = "points",interval = 10, retain = 50)
sun.mass = 2e30
earth.mass = 1e24
sun.momentum = sun.mass*vector(0,0,-1e-2)
earth.momentum = -sun.momentum

dt = 1e5

while True:
    rate(200)
    r = earth.pos - sun.pos
    F = G * sun.mass * earth.mass * r.hat / mag(r)**2
    sun.momentum += F*dt
    sun.pos += (sun.momentum/sun.mass)*dt
    earth.momentum -= F*dt
    earth.pos += (earth.momentum/earth.mass)*dt
    earth.rotate(angle = 23.5)
    
    



