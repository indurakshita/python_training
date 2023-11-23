
# # NameError
# abc

# # Syntaxt error
# abc +

# # ZeroDivisionError 
# a = 10/0

# # TypeError
# a = "b"
# c = 3
# d = a + c

# # IndexError
# a = [1,2,3]
# a[5]

# # AttributeError
# class Some:
#     def __init__(self):
#         ...

# s = Some()
# s.read()

# # KeyError
# d = {"a": 1, "b": 2}
# d["c"]

# # AssertionError
# assert 2==3


# # IndentationError
# def exa():
#     h = None
#      g = 5


# # MemoryError
# a = [i for i in range(9999999999999999999999999999999999999999999999999999)]

# # NotImplementedError
# def new():
#     raise NotImplementedError 
# new()


# a = "hello world"

# if "hello" in a:
#     raise SyntaxError("hello is not a valid input")


# Create custom error classes

# Simple Error Handling
class SimpleError(Exception):
    __module__ = Exception.__module__



# raise SimpleError('This is a simple error')
# raise SimpleError('This is a simple error')
# raise SimpleError('This is a simple error')

# # Complex Error handling
# class MyError(Exception):
#     __module__ = Exception.__module__
    
#     def __init__(self, message=None, good=True):
#         self.message = message
#         self.good = good
        
#     def __str__(self) -> str:
#         status = 'GOOD' if self.good else 'BAD'
#         if not self.message:
#             self.message = f"This is default {status} message".format(status=status)
        
#         return self.message.format(status=status)


# # raising errors
# raise MyError("this is a very {status} example", good=False)


# try:
#     num_1 = int(input("Num 1: "))
#     num_2 = int(input("Num 2: "))

#     out = num_1 / num_2
#     print(out)
    
# # except ValueError as error:
# #     print("Please check your input")

# # except ZeroDivisionError as error:
# #     print("Please check your input No zeros allowed")

# except (ValueError, ZeroDivisionError) as error:
#     print(str(error))

# lst = ["apple", "mango", 2, 3, 4, "orange"]

# for item in lst:
#     try:
#         print(item.capitalize())
#     except:
#         print("Skipping")
#         continue

        