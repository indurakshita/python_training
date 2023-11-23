class FlyweightFactory:
    _flyweights = {}

    def get_flyweight(self, key):
        if key not in self._flyweights:
            self._flyweights[key] = ConcreteFlyweight(key)
        return self._flyweights[key]

class ConcreteFlyweight:
    def __init__(self, key):
        self._key = key

    def operation(self):
        print(f"Concrete Flyweight with key '{self._key}' is used.")

class Client:
    def __init__(self):
        self._factory = FlyweightFactory()
        self._flyweights = []

    def add_flyweight(self, key):
        self._flyweights.append(self._factory.get_flyweight(key))

    def operation(self):
        for flyweight in self._flyweights:
            flyweight.operation()

if __name__ == "__main__":
    client = Client()
    client.add_flyweight("A")
    client.add_flyweight("B")
    client.add_flyweight("A")
    client.operation()