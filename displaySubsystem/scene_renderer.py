class SceneRenderer:
    def __init__(self, ds):
        self.ds = ds
        self.ctx = ds.ctx
        self.mesh = ds.mesh
        self.scene = ds.scene
        # depth buffer
        self.depth_texture = self.mesh.texture.textures['depth_texture']
        self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)

    def render_shadow(self):
        self.depth_fbo.clear()
        self.depth_fbo.use()
        for obj in self.scene.objects:
            if obj!=None:
                obj.render_shadow()

    def main_render(self):
        self.ds.ctx.screen.use()
        for obj in self.scene.objects:
            if obj!=None:
                obj.render()

    def render(self):
        self.scene.update()
        # pass 1
        self.render_shadow()
        # pass 2
        self.main_render()

    def destroy(self):
        self.depth_fbo.release()