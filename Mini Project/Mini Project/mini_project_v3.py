# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:11:41 2020

@author: Gyalpo
"""


from vpython import *


scene.forward = vector(0,-.3,-1)

G = 6.7e-11 # Newton gravitational constant

giant = sphere(pos=vector(0,0,0), radius=2e10, 
                make_trail=True, trail_type='points', interval=10, retain=10, texture="https://i.imgur.com/ejXbe1E.jpg")
giant.mass = 2e30
giant.p = vector(0, 0, 1e-2) * giant.mass

dwarf = sphere(pos=vector(1.5e11,0,0), radius=1e10,
                make_trail=True, trail_type='points', interval=10, retain=10, texture="https://i.imgur.com/dl1sA.jpg")
dwarf.mass = 1e24
dwarf.p = -giant.p


dt = 1e5
while True:
    rate(50)
    r = dwarf.pos - giant.pos
    F = G * giant.mass * dwarf.mass * r.hat / mag(r)**2
    giant.p = giant.p + F*dt
    dwarf.p = dwarf.p - F*dt
    giant.pos = giant.pos + (giant.p/giant.mass) * dt
    dwarf.pos = dwarf.pos + (dwarf.p/dwarf.mass) * dt
    dwarf.rotate(angle = 0.4,axis = vector(1,1,0))
    giant.rotate(angle=0.01, axis = vector(0,1,0))
