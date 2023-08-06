from vectors import *
from math import *
import matplotlib.cm
from OpenGL.GLU import *

def add(v1,v2):
   return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])

def subtract(v1,v2):
   return (v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2])

def cross(u, v):
     ux,uy,uz = u
     vx,vy,vz = v
     return (uy*vz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx)


def dot(u,v):
     return sum([coord1 * coord2 for coord1,coord2 in zip(u,v)])


def scale(scalar,v):
     return tuple(scalar * coord for coord in v)


def length(v):
     return sqrt(sum([coord ** 2 for coord in v]))


def unit(v):
     return scale(1./length(v), v)


def normal(face):
     return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

samplecmap = matplotlib.cm.get_cmap('Purples')
def shade(face,light=(1,2,3),color_map=samplecmap):
     return color_map(1 - dot(unit(normal(face)), unit(light)))
     
     