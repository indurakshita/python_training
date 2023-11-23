# creational pattern - Singleton


# class Singleton(type):
#     _instances = {} # {database: database(object)}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#         return cls._instances[cls]
        


class CustomException(Exception):
    __module__ = Exception.__module__

class Singleton(type):
    _instances = None
    def __call__(cls, *args, **kwargs):
        if not cls._instances:
            cls._instances = super().__call__(*args, **kwargs)
        else:
            raise CustomException("already instantiated cannot create more than once")
        return cls._instances
        

class Database(metaclass=Singleton):
    def __init__(self, database) -> None:
        self.database = database
        
    def save(self):
        print(self.database)
        

class New(metaclass=Singleton):
    def __init__(self, new) -> None:
        self.new = new
        
    def save(self):
        print(self.new)
        
        
db = Database("some_data")
db.save()
db = Database("some_other")
db.save()
