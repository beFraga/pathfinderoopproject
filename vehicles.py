class Vehicles:
    def __init__(self, mytype, price, name) -> None:
        self.mytype:    int = mytype
        self.price:     int = price
        self.name:      str = name

    def moveFor(self, local) -> None: # to do
        print(f'You moved in a(n) {self.name} to {local}')

    def __str__(self):
        return f'Type: {self.mytype} | Name: {self.name} | Price: {self.price}/um'


class Car(Vehicles):
    def __init__(self, mytype=1, price=10, name='Car') -> None:
        super().__init__(mytype, price, name)


class Helicopter(Vehicles):
    def __init__(self, mytype=2, price=30, name='Helicopter') -> None:
        super().__init__(mytype, price, name)

    def moveFor(self, local) -> None:
        print(f'You moved for a helipoint and after went to {local}')

allV = [Car(), Helicopter()]