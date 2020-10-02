from vpython import*
import numpy as np
import math

#These are the orbital elements from my best run of Method of Gauss (1,4,5)
a=2.2485029658833775
e=0.3192097798094183
i=math.radians(5.248230217512295)
omega=math.radians(170.6537147885333)
w=math.radians(142.62268502412667)
M=math.radians(347.3824586342619)
ae=1.00000011
ee=0.01671022
ie=math.radians(0.00005)
omegae=math.radians(-11.26064)
we=math.radians(102.94719)
Me=math.radians(100.46435)


def solvekepasteroid(M):
    Eguess = M #Your first guess for E is M. 
    Mguess = Eguess - e*sin(Eguess)
    Mtrue = M 
    while abs(Mguess - Mtrue) > 1e-004: #change to greater then
        Mguess = Eguess - e*math.sin(Eguess)
        Eguess = Eguess - (Mtrue + e*math.sin(Eguess) - Eguess) / (e*math.cos(Eguess)-1)
    return Eguess

def solvekepEarth(Me):
    Eguesse = Me #Your first guess for E is M. 
    Mguesse = Eguesse - e*sin(Eguesse)
    Mtruee = Me
    while abs(Mguesse - Mtruee) > 1e-004: #change to greater then
        Mguesse = Eguesse - ee*sin(Eguesse)
        Eguesse = Eguesse - (Mtruee + ee*math.sin(Eguesse) - Eguesse) / (ee*math.cos(Eguesse)-1)
    return Eguesse
#initialize variables that will be needed later and delete unneeded variables (dt)
sqrtmu = 0.01720209895
mu = sqrtmu**2
period = math.sqrt(4*pi**2*a**3/mu)
periode = math.sqrt(4*pi**2*ae**3/mu)
time = 0
r1ecliptic = vector(0, 0, 0)
earthpos= vector(0,0,0)




#create matrices to spin vector (step4)
def matrixmulast(x,y,z):
    
    matrix0=np.array([x,y,z])
    matrix1=np.array([[math.cos(w),-math.sin(w), 0],
              [math.sin(w), math.cos(w), 0],
              [0, 0, 1]])
    matrix2=np.array([[1, 0, 0],
                [0, math.cos(i), -math.sin(i)],
               [0, math.sin(i), math.cos(i)]])
    matrix3=np.array([[math.cos(omega), -math.sin(omega), 0],
               [math.sin(omega), math.cos(omega), 0],
               [0,0,1]])
    step1=np.matmul(matrix0, matrix1)
    step2=np.matmul(step1, matrix2)
    step3=np.matmul(step2, matrix3)
    r1ecliptic=vector(step3[0],step3[1],step3[2])
    return(r1ecliptic)

def matrixmulearth(x,y,z):
    
    matrix0=np.array([x,y,z])
    matrix1=np.array([[math.cos(we),-math.sin(we), 0],
              [math.sin(we), math.cos(we), 0],
              [0, 0, 1]])
    matrix2=np.array([[1, 0, 0],
                [0, math.cos(ie), -math.sin(ie)],
               [0, math.sin(ie), math.cos(ie)]])
    matrix3=np.array([[math.cos(omegae), -math.sin(omegae), 0],
               [math.sin(omegae), math.cos(omegae), 0],
               [0,0,1]])
    step1=np.matmul(matrix0, matrix1)
    step2=np.matmul(step1, matrix2)
    step3=np.matmul(step2, matrix3)
    earthpos=vector(step3[0],step3[1],step3[2])
    return(earthpos)


asteroid = sphere(pos=r1ecliptic*150, radius=(15), texture="https://i.imgur.com/VnHkOzo.jpg")
asteroid.trail = curve(color=color.white)
sun = sphere(pos=vector(0,0,0), radius=(50), texture="https://i.imgur.com/ejXbe1E.jpg")

earth= sphere(pos=earthpos*150, radius=(25), texture="https://i.imgur.com/dl1sA.jpg" )
earth.trail = curve(color=color.white)

while "nocollision"=="nocollision":
    rate(100)
    time = time + 1
    Mtrue = 2*pi/period*(time) + M
    Etrue = solvekepasteroid(Mtrue)
    Mtruee = 2*pi/periode*(time) +Me
    Etruee= solvekepEarth(Mtruee)
    x=a*math.cos(Etrue)-a*e
    y=a*(math.sqrt(1-e**2))*math.sin(Etrue)
    z=0
    xe=ae*math.cos(Etruee)-ae*ee
    ye=ae*(math.sqrt(1-ee**2))*math.sin(Etruee)
    ze=0
    r1ecliptic=matrixmulast(x,y,z)
    earthpos=matrixmulearth(xe,ye,ze)
    asteroid.pos = r1ecliptic*150 
    asteroid.trail.append(pos=asteroid.pos) 
    earth.pos= earthpos*150
    earth.trail.append(pos=earth.pos)


