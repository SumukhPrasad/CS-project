from displaySybsystem.main import *
from displaySybsystem.dsHelpers import *
from pywavefront import Wavefront

scene = Wavefront('models/toy_car.obj')
scene_box = (scene.vertices[0], scene.vertices[0])
for vertex in scene.vertices:
    min_v = [min(scene_box[0][i], vertex[i]) for i in range(3)]
    max_v = [max(scene_box[1][i], vertex[i]) for i in range(3)]
    scene_box = (min_v, max_v)
scene_trans    = [-(scene_box[1][i]+scene_box[0][i])/2 for i in range(3)]

scaled_size    = 5
scene_size     = [scene_box[1][i]-scene_box[0][i] for i in range(3)]
max_scene_size = max(scene_size)
scene_scale    = [scaled_size/max_scene_size for i in range(3)]


from OpenGL.GL import *
from OpenGL.GLU import *

def runner():
     glClearColor(0.7, 0.75, 0.75, 1)
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     glMatrixMode(GL_PROJECTION)
     glLoadIdentity()
     glMatrixMode(GL_MODELVIEW)
     glLoadIdentity()
     glEnable(GL_DEPTH_TEST)

     glBegin(GL_TRIANGLES)
     glPushMatrix()

     for mesh in scene.mesh_list:
          glBegin(GL_TRIANGLES)
          for face in mesh.faces:
               for vertex_i in face:
                    glVertex3f(*scene.vertices[vertex_i])
          glEnd()

     glPopMatrix()
     glEnd()

ds = DisplaySubsystem(512, 512, "inferno", runner)