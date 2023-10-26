import numpy as np
import glm

import pygame as pg

class OpenGLModel:
     def __init__(self, ds, name):
          self.ds=ds
          self.ctx=ds.ctx
          self.name=name
          self.vertex_buffer_object = self.get_vertex_buffer_object()
          self.shader_program = self.get_shader_program()
          self.vertex_array_object = self.get_vertex_array_object()
          self.texture = self.get_texture()

          self.m_model = self.get_model_matrix()

          self.initialize()

     def get_model_matrix(self):
          m_model = glm.mat4()
          return m_model
     
     def get_texture(self):
           texture=pg.image.load(f'models/textures/{self.name}.png').convert()
           texture = pg.transform.flip(texture, flip_x=False, flip_y=True) # correct Y-axis
           texture = self.ctx.texture(size=texture.get_size(), components=3, data=pg.image.tostring(texture, 'RGB'))
           return texture

     def initialize(self):
          self.shader_program['u_texture_0'] = 0
          self.texture.use()

          self.shader_program['m_proj'].write(self.ds.camera.m_proj)
          self.shader_program['m_view'].write(self.ds.camera.m_view)
          self.shader_program['m_model'].write(self.m_model)

     def update(self):
          m_model = glm.rotate(self.m_model, self.ds.time, glm.vec3(0,1,0))
          self.shader_program['m_model'].write(m_model)

     def get_vertex_array_object(self):
          vertex_array_object = self.ctx.vertex_array(self.shader_program, [(self.vertex_buffer_object, '2f 3f', 'in_texcoord_0', 'in_position')])
          return vertex_array_object
     
     def render(self):
          self.update()
          self.vertex_array_object.render()

     def destroy(self):
          self.vertex_buffer_object.release()
          self.shader_program.release()
          self.vertex_array_object.release()

     def get_vertex_data(self):
          vertices = [(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1),(-1,1,-1),(-1,-1,-1),(1,-1,-1),(1,1,-1)]
          indices = [
               (0,2,3),(0,1,2),
               (1,7,2),(1,6,7),
               (6,5,4),(4,7,6),
               (3,4,5),(3,5,0),
               (3,7,4),(3,2,7),
               (0,6,1),(0,5,6)
          ]
          vertex_data = self.generate_vertex_data(vertices, indices)

          tex_coord = [(0, 0),(1, 0), (1, 1), (0, 1)]
          tex_coord_indices = [(0,2,3),(0,1,2),
                               (0,2,3),(0,1,2),
                               (0,1,2),(2,3,0),
                               (2,3,0),(2,0,1),
                               (0,2,3),(0,1,2),
                               (3,1,2),(3,0,1)]
          tex_coord_data = self.generate_vertex_data(tex_coord, tex_coord_indices)
          vertex_data = np.hstack([tex_coord_data, vertex_data])

          return vertex_data
     
     @staticmethod
     def generate_vertex_data(vertices,indices):
          data = [vertices[i] for triangle in indices for i in triangle]
          return np.array(data, dtype='f4')

     def get_vertex_buffer_object(self):
          vertext_data = self.get_vertex_data()
          vbo=self.ctx.buffer(vertext_data)
          return vbo
     
     def get_shader_program(self):
          with open(f'models/shaders/{self.name}.vert') as file:
                    vertex_shader = file.read()
          with open(f'models/shaders/{self.name}.frag') as file:
                    fragment_shader = file.read()
          program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
          return program
     