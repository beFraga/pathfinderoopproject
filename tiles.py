class Tiles:
    def __init__(self, pos, move, name) -> None:
        self.f_val = 0
        self.g_val = 0
        self.pos = pos
        self.move = move
        self.name = name
    
    def __str__(self):
        return f'{self.pos} F{self.f_val} G{self.g_val} {self.name} | '

startpoint = lambda pos: Tiles(pos, 0, "O")
endpoint = lambda pos: Tiles(pos, 0, "X")
block = lambda pos: Tiles(pos, 2, "|")
floortile = lambda pos: Tiles(pos, 0, "#")
water = lambda pos: Tiles(pos, 2, "~")
bridge = lambda pos: Tiles(pos, 1, "=")
helipoint = lambda pos: Tiles(pos, 0, "H")

__all__ = ["startpoint", "endpoint", "block", "floortile", "water", "bridge", "helipoint"]