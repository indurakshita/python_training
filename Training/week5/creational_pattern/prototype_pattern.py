import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype(Prototype):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"ConcretePrototype with value: {self.value}"

if __name__ == "__main__":
    prototype = ConcretePrototype(10)
    clone = prototype.clone()

    print(f"Original: {prototype}")
    print(f"Clone: {clone}")