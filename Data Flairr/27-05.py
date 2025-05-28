# def asmd(a,b):
#     c= a + b
#     d= a - b
#     e= a * b
#     f= a / b
#     return c, d, e, f

# print(asmd(10, 20))  # Output: (30, -10, 200, 0.5)
# FUnction as an Argument

def display(func):
    return 'parth is ' + func
def name():
    return 'parth'

# Passing function as an argument
print(display(name()))  # Output: parth is parth


