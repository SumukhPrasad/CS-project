from displaySubsystem.model import *
class Scene:
    def __init__(self, ds):
        self.ds = ds
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        ds = self.ds
        add = self.add_object
        
        # self.monkey = ObjectModel(ds, vertex_array_object_name="monkey", tex_id="monkey", pos=(0, -1, -10))
        # add(self.monkey)
        
        self.board = ObjectModel(ds, vertex_array_object_name="board", tex_id="board", pos=(0, -1, -10))
        add(self.board)

    def update(self):
       pass
        #self.monkey.rot.xyz = self.ds.time
