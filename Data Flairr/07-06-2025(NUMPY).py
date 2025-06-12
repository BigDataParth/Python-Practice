import numpy as np

# myar = np.array([1, 50, 3, 4, 5])
# print(myar)
# print(type(myar))

# myar.sort()
# print(myar)

# myar =np.ones(3)
# print(myar)

# myar =np.arange(0, 10, 5)
# print(myar)

myar1 =np.array([1, 2, 3, 4, 5])
myar2 =np.array([6, 2, 8, 9, 10])
myar3 =myar1 != myar2
# print((myar3))
# print(all(myar3))

myar3 =np.where(myar1 >3 , myar1,0)
print(myar3)
