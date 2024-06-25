class Vehicles:
    def __init__(self, mytype, price, name) -> None:
        self.mytype:    int = mytype
        self.price:     int = price
        self.name:      str = name

    def moveFor(self, maze) -> None:  # to do
        res = maze.aStar(self.mytype, maze.start, maze.end)
        if not res:
            return 'There is no possible path in this map', False
        return res, True
        

    def __str__(self):
        return f'Type: {self.mytype} | Name: {self.name} | Price: {self.price}/um'


class Car(Vehicles):
    def __init__(self, mytype=1, price=10, name='Car') -> None:
        super().__init__(mytype, price, name)


class Helicopter(Vehicles):
    def __init__(self, mytype=2, price=30, name='Helicopter') -> None:
        super().__init__(mytype, price, name)

    def moveFor(self, maze) -> None:
        res1 = maze.aStar(1, maze.start, maze.helipoint)
        if not res1:
            return 'There is no possible path to helipoint in this map', False
        print('ok')
        res2 = maze.aStar(self.mytype, maze.helipoint, maze.end)
        if not res2:
            return 'There is no possible path to end in this map', False
        res = (res1[0] + res2[0], set(res1[1] + res2[1]))
        return res, True


class Truck(Vehicles):
    def __init__(self, mytype=0, price=20, name='Truck') -> None:
        super().__init__(mytype, price, name)


allV = [Car(), Helicopter(), Truck()]
