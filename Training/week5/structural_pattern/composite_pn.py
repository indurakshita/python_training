class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        results = []
        for child in self.children:
            results.append(child.operation())
        return f"Composite([{', '.join(results)}])"

if __name__ == "__main__":
    leaf1 = Leaf()
    leaf2 = Leaf()

    composite = Composite()
    composite.add(leaf1)
    composite.add(leaf2)

    composite2 = Composite()
    composite2.add(composite)
    composite2.add(Leaf())

    print(composite2.operation())