def add(*args):
    addition = 0
    for i in args:
        addition += i
    return addition


print(add(5, 5, 5, 5, 5))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
