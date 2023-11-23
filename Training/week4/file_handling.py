

# file handling (Default)
# Opening


file_handler = open("functions.pys", "w")

# Writing
write_handler = file_handler.write('print("Hello world! This file was updated dynamically using code!")')

# Closing
file_handler.close()


# # Reading
# file_handler = open("functions.pys", "r")
# code = file_handler.read()



# Closing
file_handler.close()

# exec(code)


# Context managers




# We are creating a context manager
# class CustomOpen:
#     def __init__(self, filename, mode="r"):
#         self.filename = filename
#         self.mode = mode
#         self.data = None
#         try:
#             self.file = open(self.filename, mode=self.mode)
#         except FileNotFoundError:
#             pass
        
        
#     def __enter__(self):
#         self.file = open(self.filename, mode=self.mode)
#         return self
    
#     def read(self):
#         self.data = self.file.read()
#         return self.data
    
#     def write(self, body=None):
#         self.file.write(body)
    
#     def close(self):
#         self.file.close()
        
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("exiting with statement")
#         self.file.close()
        

# Context manager
# with CustomOpen("functions.pys") as f:
#     data = f.read()
#     print(data)


# f = CustomOpen("functions.pys")

# data = f.read()
# print(data)
# f.close()


# __enter__ and __exit__ methods are mandatory
# class Myclass:
  
#     def __enter__(self):
#         print("I have entered the program")
    
        
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("I am exiting the program")

# with Myclass() as mc:
#     ...