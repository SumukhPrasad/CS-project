import moderngl as mgl
import numpy as np
import glm

class BaseModel:
    def __init__(self, ds, vertex_array_object_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.ds = ds
        self.pos = pos
        self.vertex_array_object_name = vertex_array_object_name
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vertex_array_object = ds.mesh.vertex_array_object.vertex_array_objects[vertex_array_object_name]
        self.program = self.vertex_array_object.program
        self.camera = self.ds.camera

    def update(self): 
        pass

    def get_model_matrix(self):
        m_model = glm.mat4()
        # translate
        m_model = glm.translate(m_model, self.pos)
        # rotate
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        # scale
        m_model = glm.scale(m_model, self.scale)
        return m_model

    def render(self):
        self.update()
        self.vertex_array_object.render()


class ExtendedBaseModel(BaseModel):
    def __init__(self, ds, vertex_array_object_name, tex_id, pos, rot, scale):
        super().__init__(ds, vertex_array_object_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use(location=0)
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def update_shadow(self):
        self.shadow_program['m_model'].write(self.m_model)

    def render_shadow(self):
        self.update_shadow()
        self.shadow_vertex_array_object.render()

    def on_init(self):
        self.program['m_view_light'].write(self.ds.light.m_view_light)
        # resolution
        self.program['u_resolution'].write(glm.vec2(self.ds.WINDOW_SIZE))
        # depth texture
        self.depth_texture = self.ds.mesh.texture.textures['depth_texture']
        self.program['shadowMap'] = 1
        self.depth_texture.use(location=1)
        # shadow
        self.shadow_vertex_array_object = self.ds.mesh.vertex_array_object.vertex_array_objects['shadow_' + self.vertex_array_object_name]
        self.shadow_program = self.shadow_vertex_array_object.program
        self.shadow_program['m_proj'].write(self.camera.m_proj)
        self.shadow_program['m_view_light'].write(self.ds.light.m_view_light)
        self.shadow_program['m_model'].write(self.m_model)
        # texture
        self.texture = self.ds.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use(location=0)
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # light
        self.program['light.position'].write(self.ds.light.position)
        self.program['light.Ia'].write(self.ds.light.Ia)
        self.program['light.Id'].write(self.ds.light.Id)
        self.program['light.Is'].write(self.ds.light.Is)


class ObjectModel(ExtendedBaseModel):
    def __init__(self, ds, vertex_array_object_name='def', tex_id='def',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(1, 1, 1)):
        super().__init__(ds, vertex_array_object_name, tex_id, pos, rot, scale)

    def update(self):
        self.m_model = self.get_model_matrix()
        super().update()