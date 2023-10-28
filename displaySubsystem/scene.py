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

        # cat
        add(ObjectModel(ds, pos=(0, -1, -10)))

    def update(self):
        pass
        #self.moving_cube.rot.xyz = self.ds.time
