from sys import displayhook
from vpython import *

scene= displayhook ('Our solarsystem')

""" attributes """
sun=sphere(pos=vector(0,0,0), radius=200, color=color.yellow, make_trail=True)
#sun.trail= (color=color.yellow)
#sun.velocity=vector(0,50,0)

mercury=sphere(pos=vector(300,0,0), radius=20,  color=color.orange)
mercury.trail=curve(color=color.orange)
mercury.velocity=vector(0,0,2300)

venus=sphere(pos=vector(600,0,0), radius=50,  color=color.magenta)
venus.trail=curve(color=color.magenta)
venus.velocity=vector(0,0,1600)

earth=sphere(pos=vector(800,0,0), radius=50, color=color.blue, )
earth.trail=curve(color=color.blue)
earth.velocity=vector(0,0,1400)

# earth's moon
#moon=sphere(pos=vector(800+30,0,0), radius=15, color=color.white)
#moon.trail=curve(color=color.white)
#moon.velocityE=vector(0,5,1400+50) # Initial velocity vector of moon in relation to earth
#moon.velocityS=earth.velocity + moon.velocityE # Initial velocity vector of moon in relation to sun as origin 
#moon.velocity=earth.velocity+vector(250,0,0)

mars=sphere(pos=vector(1200,0,0), radius=45,  color=color.red)
mars.trail=curve(color=color.red)
mars.velocity=vector(0,0,1100)

jupiter=sphere(pos=vector(1800,0,0), radius=75, color=color.cyan)
jupiter.trail=curve(color=color.cyan)
jupiter.velocity=vector(0,0,900)

saturn=sphere(pos=vector(2200,0,0), radius=60, color=color.orange)
saturn.trail=curve(color=color.orange)
saturn.velocity=vector(0,0,800)

uranus=sphere(pos=vector(3200,0,0), radius=50, color=color.green)
uranus.trail=curve(color=color.green)
uranus.velocity=vector(0,0,620)

neptune=sphere(pos=vector(4000,0,0), radius=50, color=color.blue)
neptune.trail=curve(color=color.blue)
neptune.velocity=vector(0,0,550)


"""constants"""
G=-6.7*10E-4# true value of G is -6.7*10E-11
m_sun=2*10E10 # all masses are true but have been scaled by a factor of 1*10E20
m_mercury=3.29*10E3
m_venus=4.87*10E4
m_earth=6*10E4
m_moon=7.35*10E2
m_mars=6.39*10E3
m_jupiter=1.9*10E7
m_saturn=5.68*10E6
m_uranus=8.68*10E5
m_neptune=1.31*10E6

#Force of Gravity:
#Fgrav= (-G*M*m*unit vector)/r**2
#Acceleration due to grav is agrav=Fgrav/m
#unit vector=vector/magnitude of vector

"""set the time intervals"""
t=0
deltat=0.01 # program computes every 0.01 seconds

# to make program run when certain conditions are met, set a while loop
while True:
    rate(40)# controls the speed of the program
   # sun.pos=sun.pos+deltat*sun.velocity


    mercury.trail.append(pos=mercury.pos)
    distance_mercury= mag(mercury.pos)
    unitvector_mercury=(mercury.pos-sun.pos)/distance_mercury
    FgravMercury=(G*m_sun*m_mercury*unitvector_mercury)/distance_mercury**2
    mercury.velocity=mercury.velocity+(FgravMercury/m_mercury)*deltat
    mercury.pos=mercury.pos+mercury.velocity*deltat
    mercury.rotate(angle=radians(10),axis=vector(0,1,0))
    if distance_mercury <= sun.radius: break

    venus.trail.append(pos=venus.pos)
    distance_venus= mag(venus.pos)
    unitvector_venus=(venus.pos-sun.pos)/distance_venus
    FgravVenus=(G*m_sun*m_venus*unitvector_venus)/distance_venus**2
    venus.velocity=venus.velocity+(FgravVenus/m_venus)*deltat
    venus.pos=venus.pos+venus.velocity*deltat
    venus.rotate(angle=radians(20),axis=vector(0,1,0))
    if distance_venus <= sun.radius: break
    
    #moon.trail.append(pos=moon.pos)
    earth.trail.append(pos=earth.pos)
    
    distance_Sun_Earth= mag(earth.pos)
    #distance_Earth_Moon= mag(moon.pos-earth.pos)
    #distance_Sun_Moon= mag (moon.pos-sun.pos)
    
    unitvector_Sun_Earth=(earth.pos-sun.pos)/distance_Sun_Earth
    #unitvector_Earth_Moon=(moon.pos-earth.pos)/distance_Earth_Moon
    #unitvector_Sun_Moon=(moon.pos-sun.pos)/distance_Sun_Moon

    
    FgravSE=(G*m_sun*m_earth*unitvector_Sun_Earth)/distance_Sun_Earth**2
    #FgravEM=(G*m_moon*m_earth*unitvector_Earth_Moon)/distance_Earth_Moon**2
    #FgravSM=(G*m_moon*m_sun*unitvector_Sun_Moon)/distance_Sun_Moon**2

    
    earth.velocity=earth.velocity+(FgravSE/m_earth)*deltat
    #moon.velocityE+=((FgravEM+FgravSM)/m_moon)*deltat
    #moon.velocityS+=(FgravSM/m_moon)*deltat+ earth.velocity
    #velocity+=((FgravEM/m_moon)+(FgravSM/m_moon))*deltat
    
    earth.pos=earth.pos+earth.velocity*deltat
    #moon.pos=moon.pos+moon.velocityS*deltat
    #moon.pos=moon.pos+moon.velocityE*deltat
    #moon.pos=moon.pos+moon.velocity*deltat

    
    earth.rotate(angle=radians(30),axis=vector(0,1,0))
    sun.rotate(angle=radians(0),axis=vector(0,1,0))
    #moon.rotate(angle=radians(15), axis=(0,1,0))
    if distance_Sun_Earth <= sun.radius: break
    
    mars.trail.append(pos=mars.pos)
    distance_mars= mag(mars.pos)
    unitvector_mars=(mars.pos-sun.pos)/distance_mars
    FgravMars=(G*m_sun*m_mars*unitvector_mars)/distance_mars**2
    mars.velocity=mars.velocity+(FgravMars/m_mars)*deltat
    mars.pos=mars.pos+mars.velocity*deltat
    mars.rotate(angle=radians(15),axis=vector(0,1,0))
    if distance_mars <= sun.radius: break

    jupiter.trail.append(pos=jupiter.pos)
    distance_jupiter= mag(jupiter.pos)
    unitvector_jupiter=(jupiter.pos-sun.pos)/distance_jupiter
    FgravJupiter=(G*m_sun*m_jupiter*unitvector_jupiter)/distance_jupiter**2
    jupiter.velocity=jupiter.velocity+(FgravJupiter/m_jupiter)*deltat
    jupiter.pos=jupiter.pos+jupiter.velocity*deltat
    jupiter.rotate(angle=radians(15),axis=vector(0,1,0))
    if distance_jupiter <= sun.radius: break

    saturn.trail.append(pos=saturn.pos)
    distance_saturn= mag(saturn.pos)
    unitvector_saturn=(saturn.pos-sun.pos)/distance_saturn
    FgravSaturn=(G*m_sun*m_saturn*unitvector_saturn)/distance_saturn**2
    saturn.velocity=saturn.velocity+(FgravSaturn/m_saturn)*deltat
    saturn.pos=saturn.pos+saturn.velocity*deltat
    saturn.rotate(angle=radians(15),axis=vector(0,1,0))
    if distance_saturn <= sun.radius: break

    uranus.trail.append(pos=uranus.pos)
    distance_uranus= mag(uranus.pos)
    unitvector_uranus=(uranus.pos-sun.pos)/distance_uranus
    FgravUranus=(G*m_sun*m_uranus*unitvector_uranus)/distance_uranus**2
    uranus.velocity=uranus.velocity+(FgravUranus/m_uranus)*deltat
    uranus.pos=uranus.pos+uranus.velocity*deltat
    uranus.rotate(angle=radians(10),axis=vector(0,1,0))
    if distance_uranus <= sun.radius: break

    neptune.trail.append(pos=neptune.pos)
    distance_neptune= mag(neptune.pos)
    unitvector_neptune=(neptune.pos-sun.pos)/distance_neptune
    FgravNeptune=(G*m_sun*m_neptune*unitvector_neptune)/distance_neptune**2
    neptune.velocity=neptune.velocity+(FgravNeptune/m_neptune)*deltat
    neptune.pos=neptune.pos+neptune.velocity*deltat
    neptune.rotate(angle=radians(20),axis=vector(0,1,0))
    if distance_neptune <= sun.radius: break


    t=t+deltat #updates time by deltat intervals
