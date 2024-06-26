from tiles import *

class Maze:
    def __init__(self, maze) -> None:
        self.maze:          list[str] = maze
        self.objectMaze:    list[list[Tiles]] = False
        self.start:         tuple = False
        self.end:           tuple = False
        self.helipoint:     tuple = False
        self.queue:         list[tuple] = []

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
                if element.name == 'X':
                    if self.end:
                        return False
                    else:
                        self.end = element.pos
                if element.name == 'H':
                    if self.helipoint:
                        return False
                    else:
                        self.helipoint = element.pos
                newLine.append(element)
            objectMaze.append(newLine)
        if not (self.end and self.start):
            return False
        self.objectMaze = objectMaze
        return True

    @staticmethod
    def gPropagation(maze, end) -> list[list[Tiles]]:
        for i, line in enumerate(maze):
            for j, value in enumerate(line):
                maze[i][j].g_val = abs(end[0] - i) + abs(end[1] - j)
                maze[i][j].f_val = float('inf')
        return maze

    def aStar(self, vehicle, start, end) -> int:
        total = []
        self.queue = [start]
        thismaze = self.objectMaze
        thismaze = Maze.gPropagation(thismaze, end)
        ij = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        while True:
            if len(self.queue) == 0:
                return False
            cur = self.queue[0]
            curobj = thismaze[cur[0]][cur[1]]
            if cur in total:
                self.queue.pop(0)
                continue
            if cur == end:
                path = []
                i = thismaze[end[0]][end[1]].path
                while i != start:
                    path.append(i)
                    i = thismaze[i[0]][i[1]].path
                return curobj.f_val, path
            for i, j in ij:
                if cur[0] + i < 0 or cur[0] + i > (len(self.maze) - 1) or cur[1] + j < 0 or cur[1] + j > (len(self.maze[0]) - 1):
                    continue
                if cur == start:
                    n1 = float('-inf')
                    n2 = 0
                else:
                    n1 = curobj.f_val
                    n2 = n1
                if thismaze[cur[0] + i][cur[1] + j].f_val + thismaze[cur[0] + i][cur[1] + j].g_val < n1 + 1 + curobj.g_val:
                    continue
                nx = thismaze[cur[0] + i][cur[1] + j]
                if vehicle < nx.move:
                    continue
                thismaze[cur[0] + i][cur[1] + j].f_val = n2 + 1
                thismaze[cur[0] + i][cur[1] + j].path = cur
                pseudoqueue = []
                inserted = False
                for k in self.queue:
                    v = thismaze[k[0]][k[1]]
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
            total.append(cur)
    
    @staticmethod
    def console(mz: list[list[Tiles]], path: list[tuple]) -> None:
        for i in mz:
            for j in i:
                color = colors.get(j.name, '?')
                if j.pos in path:
                    color = colors['o']
                print(f'{color}  ', end='')
            print('\033[0m', end='\n')


newMaze = [
    "||pppppp||",
    "||p||~|p||",
    "||ppp=pp||",
    "||p||~pppH",
    "||X||~|O||",
]


newMaze = [
    "||||||||||||||||||||||||||||||||||||||||||||||||||",
    "||||||||||||||||||||||||||||||||||||||||||||||||||",
    "|Xpppppppppppp|||||||||pppppppppppppppppppppppp|||",
    "|||||||||||||p|||||||||p||||||||||||||||||||||p|||",
    "|||pppppp||||p||pppppppp|pppp||||pp|||||||||||p|||",
    "||||p|||p||||p||p|||||||||||pppppp||||ppppppppp|||",
    "||||p|||ppppppppp||||||||||||||||p||||p|||||||||||",
    "||||p|||p|||||~~~~~~~~~~~~~~~~~~~p||||p|||||||||||",
    "||ppp|||pppppp===================pppppppH|||||||||",
    "||||||||||||||~~~~~~~~~~~~~~~~~~~|||||O|||||||||||",
]

types = {"O": startpoint, "X": endpoint, "|": block, "~": water, "=": bridge, "H": helipoint, "default": floortile}
colors = {'O': '\033[42m', 'X': '\033[45m', '|': '\033[40m', '~': '\033[46m', '=': '\033[47m', 'H': '\033[41m', '#': '\033[44m', 'o': '\033[43m'}