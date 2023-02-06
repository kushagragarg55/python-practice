class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return 'a {} car'.format(self.color)

    def __repr__(self):
        return '_'


my_car = Car("red", 3287)

print(my_car)



