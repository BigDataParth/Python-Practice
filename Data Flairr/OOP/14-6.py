# class Test:
#     def display(self):
#         self.name = "Data Flairr"
#         print("This is a test class")

#     def show(self):
#         print("This is a show method")
#         print(self.name)

# T = Test()
# T.display()
# T.show()

# class demo:
#     def __init__(self):
#         self.name = "Data Flairr"
#         print("This is a demo class")

#     def show(self):
#         print("This is a show method")
#         print(self.name)

# D = demo()
# D.show()


class Test:
    def __init__(self):
        # self.name = "Data Flairr"
        print("This is a test class constructor")

    def show(self):
        print("This is a show method")
        print(self.name)
    
    def __str__(self):
        return "This is a test class string representation"
       
T = Test()
print(T)