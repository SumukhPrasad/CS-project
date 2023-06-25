from displaySybsystem.main import *

from OpenGL.GL import *

def runner():
     glClearColor(0.7, 0.75, 0.75, 1)
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

     glBegin(GL_TRIANGLES)
     glVertex3f(-0.5, -0.5, 0.0)
     glVertex3f(0.5, -0.5, 0.0)
     glVertex3f(0.0, 0.5, 0.0)
     glEnd()

ds = DisplaySubsystem(512, 512, "hello insanity", runner)
