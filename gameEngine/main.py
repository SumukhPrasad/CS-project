class GameEngine:
     def __init__(self, grid):
          self.grid = grid

     def update(self):
          newGrid = [[self.grid[i][j] for j in range(len(self.grid[0]))] for i in range(len(self.grid))]

          def safeCell(i, j):
               try:
                    assert i>-1 and j>-1 # prevent back-indexes
                    return self.grid[i][j]
               except:
                    return 0

          for i in range(len(self.grid)):
               for j in range(len(self.grid[0])):
                    total = 0
                    cells_to_check=[
                         [i-1, j-1],
                         [i-1, j],
                         [i-1, j+1],
                         [i, j-1],
                         [i, j+1],
                         [i+1, j-1],
                         [i+1, j],
                         [i+1, j+1],
                    ]
                    for cell in cells_to_check:
                         total+=safeCell(cell[0], cell[1])
                    
                    if safeCell(i, j):
                         if (total < 2) or (total > 3):
                              newGrid[i][j] = 0
                    else:
                         if total == 3:
                              newGrid[i][j] = 1

          self.grid = newGrid