class Tiles:
    def __init__(self, pos, move, name) -> None:
        self.heuristic = 0
        self.g_val = 0
        self.pos = pos
        self.move = move
        self.name = name


startpoint = lambda pos: Tiles(pos, 0, "O")
endpoint = lambda pos: Tiles(pos, 0, "X")
wall = lambda pos: Tiles(pos, 2, "|")
floortile = lambda pos: Tiles(pos, 0, "#")
water = lambda pos: Tiles(pos, 2, "~")
bridge = lambda pos: Tiles(pos, 1, "=")
helipoint = lambda pos: Tiles(pos, 0, "H")

__all__ = ["startpoint", "endpoint", "wall", "floortile", "water", "bridge", "helipoint"]