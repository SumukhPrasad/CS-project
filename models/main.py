import numpy as np

class OpenGLModel:
     def __init__(self, ds, name):
          self.ds=ds
          self.ctx=ds.ctx
          self.name=name
          self.vertex_buffer_object = self.get_vertex_buffer_object()
          self.shader_program = self.get_shader_program()
          self.vertex_array_object = self.get_vertex_array_object()

     def get_vertex_array_object(self):
          vertex_array_object = self.ctx.vertex_array(self.shader_program, [(self.vertex_buffer_object, '3f', 'in_position')])
          return vertex_array_object
     
     def render(self):
          self.vertex_array_object.render()

     def destroy(self):
          self.vertex_buffer_object.release()
          self.shader_program.release()
          self.vertex_array_object.release()

     def get_vertex_data(self):
          vertex_data = np.array([(-0.6,-0.8,0.0),(0.6,-0.8,0.0),(0.0,0.8,0.0)], dtype='f4')
          return vertex_data
     
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
     