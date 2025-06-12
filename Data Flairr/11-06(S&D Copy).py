import numpy as np

myar1 = np.array([1, 2, 3, 4, 5])

ar =myar1.view()

print(id(myar1))
print(id(ar))

# ar1 =myar1.copy()
# ar1[2]=200
# print(myar1)
# print(ar1)

########################################################################################################

# SHALLOW AND DEEP COPY

mylist1 = [1, 2, 3, 4, 5,[6, 7, 8, 9, 10]]
# mylist2 = mylist1.copy()  # Shallow copy
# mylist1[-1][0] = 100  # Modifying the nested list in mylist1
# print(mylist2)

# import copy
# mylist2 = copy.deepcopy(mylist1)  # Deep copy
# mylist1[-1][0] = 100  # Modifying the nested list in mylist1
# print(mylist2)

