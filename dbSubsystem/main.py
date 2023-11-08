from dbSubsystem.basedb import BaseDB

class dbSubsystem:
     def __init__(self):
          self.basedb = BaseDB()

     def saveGame(self, gameboard, name):
          if self.retrieveGame(name):
               self.basedb.executesql(f'DELETE FROM games WHERE name=\'{name}\'')
          self.basedb.executesql(f"INSERT INTO games(name, game) VALUES ('{name}', '{''.join(str(element) for row in gameboard for element in row)}')")

     def retrieveGame(self, name):
          q=self.basedb.executesql(f'SELECT name, game FROM games WHERE name=\'{name}\' LIMIT 0, 1')
          if len(q)==0:
               return False
          c=q[0]
          return [list(map(int, list(c[1][i:i+8]))) for i in range(0, len(c[1]), 8)]


