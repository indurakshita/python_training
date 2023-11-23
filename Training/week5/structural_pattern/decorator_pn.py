class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

if __name__ == "__main__":
    coffee = Coffee()
    print("Cost of Coffee:", coffee.cost())

    milk_coffee = MilkDecorator(coffee)
    print("Cost of Milk Coffee:", milk_coffee.cost())

    sugar_milk_coffee = SugarDecorator(milk_coffee)
    print("Cost of Sugar Milk Coffee:", sugar_milk_coffee.cost())