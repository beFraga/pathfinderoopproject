from tiles import *

class Maze:
    def __init__(self, maze) -> None:
        self.maze = maze
        self.objectMaze = False
        self.start = False
        self.end = False
    
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
                        self.start = True
                if element.name == 'X':
                    if self.end:
                        return False
                    else:
                        self.end = True
                newLine.append(element)
            objectMaze.append(newLine)
        if not (self.end and self.start):
            return False
        self.objectMaze = objectMaze
        return True
    
    def console(self) -> None:
        if self.objectMaze:
            for i in self.objectMaze:
                string = ""
                for j in i:
                    string += j.name
                print(string)


newMaze = [
    "||O|",
    "C~=~",
    "D~=~",
    "HX H"
]

types = {"O": startpoint, "X": endpoint, "|": block, "~": water, "=": bridge, "H": helipoint, "default": floortile}