class Animal:
    __endagered = False
    def __init__(self,name):
        self.__name = name
    
    def __process(self):
        self.__name = self.__name.upper()

    def walk(self):
        self.__process()
        return f"{self.__name} is walking..."

dog = Animal("dog")