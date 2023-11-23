# Scopes

"""
Local: If you refer to x inside a function, then the interpreter first searches for it in the innermost scope that's local to that function.

Enclosing: If x isn't in the local scope but appears in a function that resides inside another function, then the interpreter searches in the enclosing function's scope.

Global: If neither of the above searches is fruitful, then the interpreter looks in the global scope next.

Built-in: If it can't find x anywhere else, then the interpreter tries the built-in scope.
"""

# Scopes hirearchy: local -> enclosing -> global -> built-in

var1 = 1 # local scope for below print statement

# print(var1)


# var1 accessible only if the condituon is true
if True:
    var2 = 200

# scope is local but it is set to last looped value
for something in range(200):
    var3 = something

# var4 is local to function and cannot be accessed from outside the scope of function
def add(num):
    """scope of var1 is global"""
    var4 = 3
    print(var4)

# add(3)

# print(var1)
num3 = 8

# enclosing
def add_multiply(num1, num2):
    num3 = num1 + num2
    
    def multiply():
        num1 = 5
        num4 = num3 * num1 # num3 is an enclosing scope for multiply function
        return num4
    return multiply()


final = add_multiply(2,3)

# print(final)


# Use globals() for checking global variable
# Use locals() for checking local variables


# Changing global variable from a local scope
glob = 5

def change_glob(num):
    global glob
    glob = num
    print(f"Printing global variable inside the function, output: {glob}")

change_glob(10)
print(f"\n\nPrinting global variable outside the function, output: {glob}")