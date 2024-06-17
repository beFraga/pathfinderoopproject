from tiles import *

class Maze:
    def __init__(self, maze) -> None:
        self.maze = maze
        self.objectMaze = maze
        self.start = False
        self.end = False
    
    def transform(self) -> bool:
        objectMaze = []
        for i,line in enumerate(self.maze):
            newLine = []
            for j,value in enumerate(line):
                element = ""
                element = types.get(value, types["default"])((i,j))
                newLine.append(element)
            objectMaze.append(newLine)
        self.objectMaze = objectMaze
        return True
    
    def console(self) -> None:
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