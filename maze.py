from tiles import *

class Maze:
    def __init__(self, maze) -> None:
        self.maze: list[list[str]] = maze
        self.objectMaze: list[list[Tiles]] = False
        self.start: tuple = False
        self.end: tuple = False
        self.queue: list[Tiles] = []
    
    def transform(self) -> bool:
        objectMaze = []
        for i,line in enumerate(self.maze):
            newLine = []
            for j,value in enumerate(line):
                element = types.get(value, types["default"])((i,j))
                if element.name == 'O':
                    if self.start:
                        return False
                    else:
                        self.start = element.pos
                if element.name == 'X':
                    if self.end:
                        return False
                    else:
                        self.end = element.pos
                newLine.append(element)
            objectMaze.append(newLine)
        if not (self.end and self.start):
            return False
        self.objectMaze = objectMaze
        return True

    def gPropagation(self) -> bool:
        print(self.start)
        print(self.end)
        for i,line in enumerate(self.objectMaze):
            for j,value in enumerate(line):
                self.objectMaze[i][j].g_val = abs(self.end[0] - i) + abs(self.end[1] - j)
        return True
    
    def console(self) -> None:
        if self.objectMaze:
            for i in self.objectMaze:
                string = ""
                for j in i:
                    string += j.__str__()
                print(string)


newMaze = [
    "||O|",
    "C~=~",
    "D~=~",
    "HX H"
]

types = {"O": startpoint, "X": endpoint, "|": block, "~": water, "=": bridge, "H": helipoint, "default": floortile}