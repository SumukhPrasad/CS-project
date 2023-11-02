import numpy as np
import moderngl as mgl
import pywavefront


class VertexBufferObject:
    def __init__(self, ctx):
        self.vertex_buffer_objects = {}
        self.vertex_buffer_objects['board'] = ObjectModelVertexBufferObject(ctx, 'displaySubsystem/objects/gameboard/model.obj')

    def destroy(self):
        [vertex_buffer_object.destroy() for vertex_buffer_object in self.vertex_buffer_objects.values()]


class BaseVertexBufferObject:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vertex_buffer_object = self.get_vertex_buffer_object()
        self.format: str = None
        self.path: str = None
        self.attribs: list = None

    def get_vertex_data(self): ...

    def get_vertex_buffer_object(self):
        vertex_data = self.get_vertex_data()
        vertex_buffer_object = self.ctx.buffer(vertex_data)
        return vertex_buffer_object

    def destroy(self):
        self.vertex_buffer_object.release()


class ObjectModelVertexBufferObject(BaseVertexBufferObject):
    def __init__(self, ds, pathtoobj):
        self.path = pathtoobj
        super().__init__(ds)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront(self.path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data