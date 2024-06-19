from maze import Maze, newMaze
from vehicles import allV, Vehicles

def println(string):
    print(f'\n{string}')

class Program:
    def __init__(self) -> None:
        self.vehicle: Vehicles = False
        self.distance: int = float('inf')
        self.maze: Maze = False

    def selectV(self) -> Vehicles:
        println('Select a vehicle: \n1. Car \n2. Helicopter')
        nV = int(input())
        if nV > len(allV) or nV < 1:
            return 'Number not in range', False
        self.vehicle = allV[nV - 1]
        return self.vehicle, True

    def createMaze(self) -> str:
        println('0. Premade map \nN M. Size of map to create')
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

    def setMaze(self) -> str:
        if not self.maze.transform():
            return '\nWas given more or less than one start and end points', False

        if not self.maze.gPropagation():
            return '??', False

        self.maze.console()
        return "\nMap transformed", True

    def runA(self) -> str:
        return 'To do runA', True
    
    def finish(self) -> str:
        return f'Distance: {self.distance} | Value: {self.distance * self.vehicle.price}', True

    def run(self) -> str:
        functions = [prog.selectV, prog.createMaze, prog.setMaze, prog.runA, prog.finish]
        for i in functions:
            msg, res = i()
            if not res:
                return msg, False
            else:
                println(msg)
            
        return 'Program totally runned', True

while True:
    prog = Program()
    msg, res = prog.run()
    println(msg)
    if res:
        break