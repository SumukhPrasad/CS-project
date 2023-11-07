from dbSubsystem.main import dbSubsystem

class gameBoard:
     def __init__(self, name):
          self.name = name
          self.dbsub = dbSubsystem()

     def save(self): ...