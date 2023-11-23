class Product:
    def __init__(self):
        self.part1 = None
        self.part2 = None

class Builder:
    def build_part1(self):
        pass

    def build_part2(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part1(self):
        self.product.part1 = "Part 1 built"

    def build_part2(self):
        self.product.part2 = "Part 2 built"

class Director:
    def construct(self, builder):
        builder.build_part1()
        builder.build_part2()

if __name__ == "__main__":
    builder = ConcreteBuilder()
    director = Director()
    director.construct(builder)
    
    product = builder.product
    print(f"Part 1: {product.part1}")
    print(f"Part 2: {product.part2}")