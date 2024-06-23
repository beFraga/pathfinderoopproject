from tiles import *


class Maze:
    def __init__(self, maze) -> None:
        self.maze:          list[str] = maze
        self.objectMaze:    list[list[Tiles]] = False
        self.start:         tuple = False
        self.end:           tuple = False
        self.queue:         list[Tiles] = []

    def transform(self) -> bool:
        objectMaze = []
        for i, line in enumerate(self.maze):
            newLine = []
            for j, value in enumerate(line):
                element = types.get(value, types["default"])((i, j))
                if element.name == 'O':
                    if self.start:
                        return False
                    else:
                        self.start = element.pos
                        self.queue.append(element.pos)
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
        for i, line in enumerate(self.objectMaze):
            for j, value in enumerate(line):
                self.objectMaze[i][j].g_val = abs(
                    self.end[0] - i) + abs(self.end[1] - j)
        return True

    def aStar(self, vehicle) -> bool:
        ij = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        while True:
            if len(self.queue) == 0:
                return False
            cur = self.queue[0]
            print("Cur: ",cur)
            curobj = self.objectMaze[cur[0]][cur[1]]
            print(curobj.path)
            if cur == self.end:
                return curobj.f_val, curobj.path
            for i, j in ij:
                if cur[0] + i < 0 or cur[0] + i > (len(self.maze) - 1) or cur[1] + j < 0 or cur[1] + j > (len(self.maze[0]) - 1):
                    continue
                if cur == self.start:
                    n1 = float('-inf')
                    n2 = 0
                else:
                    n1 = curobj.f_val
                    n2 = n1
                if self.objectMaze[cur[0] + i][cur[1] + j].f_val < n1 + 1:
                    continue
                nx = self.objectMaze[cur[0] + i][cur[1] + j]
                if vehicle.mytype < nx.move:
                    continue
                self.objectMaze[cur[0] + i][cur[1] + j].f_val = n2 + 1
                self.objectMaze[cur[0] + i][cur[1] + j].path = curobj.path
                if cur != self.start and cur not in curobj.path:
                    self.objectMaze[cur[0] + i][cur[1] + j].path.append(cur)
                print(nx)
                print(nx.path)
                pseudoqueue = []
                inserted = False
                for k in self.queue:
                    v = self.objectMaze[k[0]][k[1]]
                    if (n1 + v.g_val > nx.f_val + nx.g_val and not inserted) and nx.pos not in pseudoqueue:
                        pseudoqueue.append(nx.pos)
                        inserted = True
                    pseudoqueue.append(k)
                    if k == self.queue[len(self.queue) - 1] and not inserted and nx.pos not in pseudoqueue:
                        pseudoqueue.append(nx.pos)
                self.queue = pseudoqueue
            for i in range(len(self.queue)):
                if self.queue[i] == cur:
                    self.queue.pop(i)
                    break

    def console(self) -> None:
        if self.objectMaze:
            for i in self.objectMaze:
                string = ""
                for j in i:
                    string += j.__str__()
                print(string)


newMaze = [
    "||pppppp||",
    "||p||~|p||",
    "||ppp=pp||",
    "||p||~|p||",
    "||X||~|O||",

]

# teste

types = {"O": startpoint, "X": endpoint, "|": block, "~": water,
         "=": bridge, "H": helipoint, "default": floortile}
