from displaySybsystem.main import *
from displaySybsystem.dsHelpers import *

from OpenGL.GL import *
from OpenGL.GLU import *

def runner():
     glClearColor(0.7, 0.75, 0.75, 1)
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

     
     glMatrixMode(GL_MODELVIEW)
     #glLoadIdentity()

     light = (1,1,1)
     faces = [
          [(1,0,0), (0,1,0), (0,0,1)],
          [(1,0,0), (0,0,-1), (0,1,0)],
          [(1,0,0), (0,0,1), (0,-1,0)],
          [(1,0,0), (0,-1,0), (0,0,-1)],
          [(-1,0,0), (0,0,1), (0,1,0)],
          [(-1,0,0), (0,1,0), (0,0,-1)],
          [(-1,0,0), (0,-1,0), (0,0,1)],
          [(-1,0,0), (0,0,-1), (0,-1,0)],
     ]
     glEnable(GL_CULL_FACE)
     glEnable(GL_DEPTH_TEST)
     glCullFace(GL_BACK)
     glRotatef(1,1,1,1)
     glBegin(GL_TRIANGLES)

     for face in faces:
         color = shade(face,light)
         for vertex in face:
             glColor3fv((color[0], color[1], color[2]))
             glVertex3fv(vertex)

     glEnd()

ds = DisplaySubsystem(512, 512, "inferno", runner)