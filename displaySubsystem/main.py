import pygame as pg
import moderngl as mgl
import sys
from displaySubsystem.model import *
from displaySubsystem.camera import Camera
from displaySubsystem.light import Light
from displaySubsystem.mesh import Mesh
from displaySubsystem.scene import Scene
from displaySubsystem.scene_renderer import SceneRenderer


class DisplaySubsystem:
	def __init__(self, winH, winW, winTitle, winIcon, gb):
		pg.init()

		# OpenGL/Pygame configuration
		self.WINDOW_SIZE = (winH, winW)
		pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
		pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
		pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
		pg.display.set_mode(self.WINDOW_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)

		self.gb=gb

		# Window configuration
		pg.display.set_caption(winTitle)
		pg.display.set_icon(pg.image.load(f'res/window_icons/{winIcon}.png'))
		
		# OpenGL configuration
		self.ctx = mgl.create_context()
		self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)

		# Timing
		self.clock = pg.time.Clock()
		self.time = 0
		self.delta_time = 0

		# lights
		self.light = Light()
		# Camera
		self.camera = Camera(self)
		# Mesh
		self.mesh = Mesh(self)
		# Scene
		self.scene = Scene(self)
		# Renderer
		self.scene_renderer = SceneRenderer(self)

	def check_events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.mesh.destroy()
				self.scene_renderer.destroy()
				pg.quit()
				sys.exit()

	def render(self):
		# clear framebuffer
		self.ctx.clear(0.7, 0.75, 0.75)
		# render scene
		self.scene_renderer.render()
		# swap buffers
		pg.display.flip()

	def get_time(self):
		self.time = pg.time.get_ticks() * 0.001

	def run(self):
		while True:
			self.get_time()
			self.check_events()
			self.camera.update()
			self.render()
			self.delta_time = self.clock.tick(60)