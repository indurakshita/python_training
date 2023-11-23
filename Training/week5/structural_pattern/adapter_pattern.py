class OldSystem:
    def legacy_method(self):
        return "Legacy method in OldSystem"


class NewSystem:
    def new_method(self):
        pass


class Adapter(NewSystem):
    def __init__(self, old_system):
        self.old_system = old_system

    def new_method(self):
        return self.old_system.legacy_method()


def client_code(system):
    result = system.new_method()
    print(result)

if __name__ == "__main__":
    old_system = OldSystem()
    adapter = Adapter(old_system)
    client_code(adapter)