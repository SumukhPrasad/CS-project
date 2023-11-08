from dbSubsystem.main import dbSubsystem
from gameEngine.main import GameEngine


class gameBoard:
     def __init__(self, name, board=None):
          self.name = name
          self.dbsub = dbSubsystem()
          self.board = [[0 for _ in range(8)] for _ in range(7)]
          if board:
               self.board = board
          if self.dbsub.retrieveGame(name):
               self.board = self.dbsub.retrieveGame(name)
          self.ge = GameEngine(self.board)

     def update(self):
          self.ge.update()
          self.board = self.ge.grid

     def save(self): 
          self.dbsub.saveGame(self.ge.grid, self.name)