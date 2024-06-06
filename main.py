from maze import Maze, newMaze

class Program:
    def run() -> None:
        maze = Maze(newMaze)
        if not maze.transform():
            return 'O programa não pode possuir dois inicios ou dois finais.'
        maze.console()
        return "\nMapa criado!"

prog = Program
message = prog.run()
print(message)