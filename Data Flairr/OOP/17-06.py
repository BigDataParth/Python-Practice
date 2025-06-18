# class Test:
#     def __init__(self,rno,name,course):
#         self.rno=rno
#         self.name=name
#         self.course=course
#         print("This is a test class constructor")

#     def show(self):
#         print("This is a show method")
#         print(self.name)
    
#     def __str__(self):
#         # This method is called when we use print() on an instance of the class
#         return f"Roll No: {self.rno}, Name: {self.name}, Course: {self.course}"
    

#     #incase we don't have __str , __repr will get called
#     def __repr__(self):
#         return f"Test({self.rno}, {self.name}, {self.course})"

# T1=Test(1,"John","Python")
# print(T1)

class Demo:
    stname = "Data Flairr"
    def __len__(self):
        x=0
        for i in self.stname:
            x+=1
        return x

D1 = Demo()
print(len(D1))  # This will call the __len__ method of the Demo class