from maze import Maze, newMaze
from vehicles import allV, Vehicles


def println(string):
    print(f'\n{string}')


class Program:
    def __init__(self) -> None:
        self.vehicle:   Vehicles = False
        self.distance:  int = float('inf')
        self.maze:      Maze = False
        self.path:      list[tuple] = False

    def selectV(self) -> Vehicles:
        println('Select a vehicle: \n1. Car \n2. Helicopter \n3.Truck')
        nV = int(input())
        if nV > len(allV) or nV < 1:
            return 'Number not in range', False
        self.vehicle = allV[nV - 1]
        return self.vehicle, True

    def createMaze(self) -> str:
        println('0. Premade map \nN M. Size of map to create (N x M grid)')
        v = list(map(int, input().split()))

        if v[0] == 0:
            self.maze = Maze(newMaze)
            return 'Default map has been set', True
        myMaze = []
        for i in range(abs(v[0])):
            newLine = input('Line: ')[:abs(v[1])].upper()
            if len(newLine) != abs(v[1]):
                return f'The len of line must be {abs(v[1])}', False
            myMaze.append(newLine)
        self.maze = Maze(myMaze)
        return 'Map created', True

    def setMaze(self) -> str:
        if not self.maze.transform():
            return '\nWas given more or less than one start and end points or more than one helipoint', False
        if not self.maze.helipoint and self.vehicle.name == 'Helicopter':
            return 'Helipoint not setted', False

        Maze.console(self.maze.objectMaze, [])
        return "\nMap transformed", True

    def runA(self) -> str:
        msg, res = self.vehicle.moveFor(self.maze)
        if not res:
            return msg, False
        self.distance, self.path = msg
        Maze.console(self.maze.objectMaze, self.path)
        return f'aStar done', True

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

        return 'Program totally executed', True


while True:
    prog = Program()
    msg, res = prog.run()
    println(msg)
    if res:
        break
