from maze import Maze, newMaze
from vehicles import allV, Vehicles

class Program:
    def __init__(self) -> None:
        self.vehicle = None
        self.distance = float('inf')
        self.maze = []

    def createMaze(self) -> str:
        print('0. Premade map \nN M. Size of map to create')
        v = list(map(int, input().split()))

        if v[0] == 0:
            self.maze = Maze(newMaze)
            return 'Default map setted', True
        myMaze = []
        for i in range(v[0]):
            newLine = input('Line: ')[:v[1]].upper()
            myMaze.append(newLine)
        self.maze = Maze(myMaze)
        return 'Map created', True

    def runA(self) -> str:
        return 'To do runA', True

    def setMaze(self) -> str:
        if not self.maze.transform():
            return '\nWas given more or less than one start and end points', False

        if not self.maze.gPropagation():
            return '??', False

        self.maze.console()
        return "\nMap transformed", True

    def selectV(self) -> Vehicles:
        print('Select a vehicle: \n1. Car \n2. Helicopter')
        nV = int(input())
        if nV > len(allV) or nV < 1:
            return 'Number not in range', False
        self.vehicle = allV[nV - 1]
        return self.vehicle, True
    
    def run(self) -> str:
        msg, res = prog.selectV()
        if not res:
            return msg
        else:
            print(msg)
        
        msg, res = prog.createMaze()
        if not res:
            return msg
        else:
            print(msg)

        msg, res = prog.setMaze()
        if not res:
            return msg
        else:
            print(msg)

        msg, res = prog.runA()
        if not res:
            return msg
        else:
            print(msg)
        
        return 'Program totally runned'


prog = Program()
print(prog.run())