from displaySybsystem.main import *
from displaySybsystem.dsHelpers import *

from OpenGL.GL import *
from OpenGL.GLU import *
from displaySybsystem.objLoader import *

import faulthandler
faulthandler.enable()

model = OBJ('models/toy_car.obj')
box = model.box()
center = [(box[0][i] + box[1][i])/2 for i in range(3)]
size = [box[1][i] - box[0][i] for i in range(3)]
max_size = max(size)
distance = 10
scale = distance / max_size
angle = 0

def runner():
     glClearColor(0.7, 0.75, 0.75, 1)
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    

ds = DisplaySubsystem(512, 512, "inferno", runner)