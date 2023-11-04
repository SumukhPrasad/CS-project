from displaySubsystem.vertex_buffer_object import VertexBufferObject
from displaySubsystem.shader_program import ShaderProgram


class VertexArrayObject:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vertex_buffer_object = VertexBufferObject(ctx)
        self.program = ShaderProgram(ctx)
        self.vertex_array_objects = {}

        self.vertex_array_objects['board'] = self.get_vertex_array_object(
            program=self.program.programs['default'],
            vertex_buffer_object=self.vertex_buffer_object.vertex_buffer_objects['board'])
        

        self.vertex_array_objects['shadow_board'] = self.get_vertex_array_object(
            program=self.program.programs['shadow_map'],
            vertex_buffer_object=self.vertex_buffer_object.vertex_buffer_objects['board'])
        
        self.vertex_array_objects['piece'] = self.get_vertex_array_object(
            program=self.program.programs['default'],
            vertex_buffer_object=self.vertex_buffer_object.vertex_buffer_objects['piece'])
        

        self.vertex_array_objects['shadow_piece'] = self.get_vertex_array_object(
            program=self.program.programs['shadow_map'],
            vertex_buffer_object=self.vertex_buffer_object.vertex_buffer_objects['piece'])

    def get_vertex_array_object(self, program, vertex_buffer_object):
        vertex_array_object = self.ctx.vertex_array(program, [(vertex_buffer_object.vertex_buffer_object, vertex_buffer_object.format, *vertex_buffer_object.attribs)], skip_errors=True)
        return vertex_array_object

    def destroy(self):
        self.vertex_buffer_object.destroy()
        self.program.destroy()