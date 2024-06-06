class Vehicles:
    def __init__(self, mytype, price, name) -> None:
        self.mytype = mytype
        self.price = price
        self.name = name

    def moveFor(self, local):
        print(f'You moved in a(n) {self.name} to {local}')


class Car(Vehicles):
    def __init__(self, mytype=1, price=10, name='Car') -> None:
        super().__init__(mytype, price, name)


class Helicopter(Vehicles):
    def __init__(self, mytype=2, price=30, name='Helicopter') -> None:
        super().__init__(mytype, price, name)

    def moveFor(self, local):
        print(f'You moved for a helipoint and after went to {local}')
