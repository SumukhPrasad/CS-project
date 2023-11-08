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
        
        self.board = ObjectModel(ds, vertex_array_object_name="board", tex_id="board", pos=(0, 0, 0))
        add(self.board)

        self.pieces = []

        for i in range(7):
            self.pieces.append([])
            for j in range(8):
                if self.ds.gb.board[i][j]:
                    self.pieces[i].append(ObjectModel(ds, vertex_array_object_name="piece", tex_id="piece", pos=(-6+( j*(12.1/8 + 0.225) ), 0.2, -5.95+( i*(10.3/7 + 0.225) )))) # (x, z, y)
                else:
                    self.pieces[i].append(None)
                '''
                          _ -5.95
                          |
                   -6 |---*---| +6.1
                          |
                          ‾ +4.35
                '''
                add(self.pieces[i][j])

    def update(self):
       pass
        #self.monkey.rot.xyz = self.ds.time
