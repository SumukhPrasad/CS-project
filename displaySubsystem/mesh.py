from displaySubsystem.vertex_array_object import VertexArrayObject
from displaySubsystem.texture import Texture

class Mesh:
    def __init__(self, ds):
        self.ds = ds
        self.vertex_array_object = VertexArrayObject(ds.ctx)
        self.texture = Texture(ds)

    def destroy(self):
        self.vertex_array_object.destroy()
        self.texture.destroy()