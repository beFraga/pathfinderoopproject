from maze import Maze, newMaze
from vehicles import allV

class Program:
    def __init__(self) -> None:
        self.vehicle = None
        self.distance = float('inf')

    def runA(self) -> None:
        return 'To do'

    def createMaze(self) -> None:
        maze = Maze(newMaze)
        if not maze.transform():
            return '\nWas given more than one start or end points'
        maze.console()
        return "\nMap created"

    def selectV(self, nV) -> None:
        self.vehicle = allV[nV]
        return self.vehicle

prog = Program()
print('Select a vehicle: \n1. Car \n2. Helicopter')
nV = int(input()) - 1
message = prog.selectV(nV)
print(message)
message = prog.createMaze()
print(message)
message = prog.runA()
print(message)