import pygame as pg
import moderngl as mgl
import numpy as np
import sys


from models.main import OpenGLModel

class DisplaySubsystem:
     def __init__(self, winH, winW, winTitle,winIcon):
          pg.init()
          self.WINDOW_SIZE=(winH, winW)

          pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
          pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
          pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

          pg.display.set_mode(self.WINDOW_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
          pg.display.set_caption(winTitle)
          pg.display.set_icon(pg.image.load(f'res/window_icons/{winIcon}.png'))

          self.ctx = mgl.create_context()
          self.clock = pg.time.Clock()

          self.scene = OpenGLModel(self, 'default')



     def poll_events(self):
          for event in pg.event.get():
               if event.type==pg.QUIT:
                    self.scene.destroy()
                    pg.quit()
                    sys.exit()

     def render(self):
          self.ctx.clear(0.7, 0.75, 0.75)
          self.scene.render()
          pg.display.flip()

     def run(self):
          while True:
               self.poll_events()
               self.render()
               self.clock.tick(60)

