class Tiles:
    def __init__(self, pos, move, name) -> None:
        self.f_val: int =           float('inf')
        self.g_val: int =           False
        self.pos:   tuple =         pos
        self.move:  int =           move
        self.name:  str =           name
        self.path:  list[tuple] =   False
    
    def __str__(self) -> str:
        return f"{self.name}"

startpoint  = lambda pos: Tiles(pos, 0, "O")
endpoint    = lambda pos: Tiles(pos, 0, "X")
block       = lambda pos: Tiles(pos, 2, "|")
floortile   = lambda pos: Tiles(pos, 0, "#")
water       = lambda pos: Tiles(pos, 2, "~")
bridge      = lambda pos: Tiles(pos, 1, "=")
helipoint   = lambda pos: Tiles(pos, 2, "H")

__all__ = ["startpoint", "endpoint", "block", "floortile", "water", "bridge", "helipoint", "Tiles"]