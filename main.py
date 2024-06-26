from maze import Maze, newMaze
from vehicles import allV, Vehicles


def println(string):
    print(f'\n{string}')

class Program:
    def __init__(self) -> None:
        self.vehicle:   list[Vehicles] = []
        self.allVeh:    bool = True
        self.curV:      int = 0
        self.distance:  int = float('inf')
        self.maze:      Maze = False
        self.path:      list[tuple] = False

    def selectV(self) -> Vehicles:
        if self.allVeh and self.curV == 0:
            self.allVeh = False
        if not self.allVeh:
            println(
                'Select a vehicle: \n0. Test all vehicles \n1. Car \n2. Helicopter \n3.Truck')
            nV = int(input())
            if nV > len(allV) or nV < 0:
                return 'Number not in range', False
            if nV == 0:
                self.allVeh = True
                for i in allV:
                    self.vehicle.append(i)
            else:
                self.vehicle.append(allV[nV - 1])
        return self.vehicle[self.curV], True

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
        if not self.maze.helipoint and self.vehicle[self.curV].name == 'Helicopter':
            return 'Helipoint has not been set', False

        Maze.console(self.maze.objectMaze, [])
        return "\nMap transformed", True

    def runA(self) -> str:
        msg, res = self.vehicle[self.curV].moveFor(self.maze)
        if not res:
            return msg, False
        self.distance, self.path = msg
        Maze.console(self.maze.objectMaze, self.path)
        return f'aStar done', True

    def finish(self) -> str:
        if self.curV == len(allV) - 1:
            self.allVeh = False
        self.curV += 1
        return f'Distance: {self.distance} | Value: {self.distance * self.vehicle[self.curV - 1].price}', True

    def run(self) -> str:
        while self.allVeh:
                functions = [prog.selectV, prog.createMaze, prog.setMaze, prog.runA, prog.finish]
                for i in functions:
                    msg, res = i()
                    if not res:
                        return msg, False
                    else:
                        println(msg)
        return 'Program fully executed', True


while True:
    prog = Program()
    msg, res = prog.run()
    println(msg)
    if res:
        break
