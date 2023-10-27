class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along...')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


myCar = Vehicle('Tesla', 'Model 3')
# print(myCar.make)
# print(myCar.model)
myCar.moves()
myCar.get_make_model()

your_car = Vehicle('Cadilac', 'Escalade')

your_car.get_make_model()


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(slef):
        print('Flies  along..')


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..')


class GolfCart(Vehicle):
    pass


cessna = Airplane('Cessna', 'Skyhawk', 'N-12343')
mack = Truck('Mack', 'Pinacle')
cessna = Airplane('Cessna', 'Skyhawk', 'N-12343')
golfwagon = GolfCart('Yahmaha', 'Gh23')


cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

golfwagon.get_make_model()
golfwagon.moves()

print('\n')

for v in (myCar, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()
