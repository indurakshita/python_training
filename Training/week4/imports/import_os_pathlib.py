import pathlib 
import os
import sys

'''How to get the current directory and file:'''

"Method 1: Find the path to the given file using Path.cwd()"
# print(pathlib.Path.cwd())

"Method 2: Find the path to the given file using pathlib.Path().absolute()"
# print(pathlib.Path().absolute())

"Method 3: Find the path to the given file using os.getcwd()"
# print('Get current working directory : ', os.getcwd())

"Method 4: Find the path to the given file using os.path.basename"
# Note:
'''Using __file__, we can also get the absolute path of the running file.
__file__ is callable while working in a file. If we try to call it from the shell interpreter, it will not work.
__file__ does not work in the Jupyter notebook.'''

# print('File name :    ', os.path.basename(__file__))
# print('Directory Name:     ', os.path.dirname(__file__))

"method 5:Get the current working directory (CWD) "
# cwd = os.getcwd() 


"Method 6: Find the path to the given file using os.path.abspath"
# print(f"file_name: {os.path.abspath(__file__)}")
# print(f'Absolute directoryname: {os.path.dirname(__file__)}')


# -----------------------------------------------------------------------------------------------------------------

"How to change files one directory to another the directory "

# src_path = os.path.join(source_dir, filename)
         
# des_path = os.path.join(des_dir,filename)

"how to change the directory"

# Changing the CWD 
# os.chdir('../')        

"How to create new directory"
# There are different methods available in the OS module for creating a directory. These are –

# os.mkdir()
# os.makedirs()

"How to get Listing out Files and Directories with Python"
# print(os.listdir())

'''Deleting Directory or Files using Python
OS module proves different methods for removing directories and files in Python. These are – '''

'''Using os.remove()
os.remove() - method in Python is used to remove or delete a file path. 
This method can not remove or delete a directory. 
If the specified path is a directory then OSError will be raised by the method.'''

# path = os.path.join(location, file) 
# os.remove(path)

'''Using os.rmdir()
os.rmdir() method in Python is used to remove or delete an empty directory.
OSError will be raised if the specified path is not an empty directory.'''
 
# path = os.path.join(parent, directory) 
# os.rmdir(path)


'''os.path.exists(): This method will check whether a file exists or not by passing the name of the file as a parameter. 
OS module has a sub-module named PATH by using which we can perform many more functions. '''
# result = os.path.exists("file_name") 