
# volume of a sphere, cube and cone
from math import pi

def sphere_vol(r):
    return (4/3) * r * r * r * pi

def cube_vol(l,w,h):
    return l * w * h

def cone_vol(r,h):
    return (pi/3) * r * r * h
