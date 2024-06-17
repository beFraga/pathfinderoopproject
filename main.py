from maze import Maze, newMaze
from vehicles import allV, Vehicles

class Program:
    def __init__(self) -> None:
        self.vehicle = None
        self.distance = float('inf')
        self.maze = []

    def createMaze(self, v) -> str:
        print('0. Premade map \nN M. Size of map to create')
        v = list(map(int, input().split()))

        if v[0] == 0:
            self.maze = Maze(newMaze)
            return 'Map setted'
        myMaze = []
        for i in range(v[0]):
            newLine = input('Line: ')[:v[1]].upper()
            myMaze.append(newLine)
        self.maze = Maze(myMaze)
        return 'Map setted'

    def runA(self) -> str:
        return 'To do runA'

    def setMaze(self) -> str:
        if not self.maze.transform():
            return '\nWas given more or less than one start and end points'
        self.maze.console()
        return "\nMap created"

    def selectV(self, nV) -> Vehicles:
        print('Select a vehicle: \n1. Car \n2. Helicopter')
        nV = int(input()) - 1
        self.vehicle = allV[nV]
        return self.vehicle

prog = Program()
print(prog.selectV())
print(prog.createMaze())
print(prog.setMaze())
print(prog.runA())