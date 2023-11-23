from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def operation(self):
        product = self.factory_method()
        return f"Creator: Created {product.operation()}"

class ConcreteProductA:
    def operation(self):
        return "Product A"

class ConcreteProductB:
    def operation(self):
        return "Product B"


class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

def main():
    creator_a = ConcreteCreatorA()
    creator_b = ConcreteCreatorB()

    print(creator_a.operation())  
    print(creator_b.operation())  

if __name__ == "__main__":
    main()