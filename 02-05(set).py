import sys
Set1 = {"A", 1, "B", 2, "C", 3}
Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}

      
# print(sys.getsizeof(Set2)) 


# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 5, 8, 4, 10]

# a = [1, 2, 3, 4, 5, 6]
# b = [4, 5, 6, 7, 8]

# for i in a:
#     if i not in  b:
#         print(i)

# s = "101012000111"

# if set(s) =={'0', '1'}:
#     print("Binary")
# else:
#     print("Not Binary")

from itertools import *
s = {1, 2, 3, 4}
k = 2

# Get all subsets of size k
subsets = list(permutations(s, k))
print("Subsets of size", k, ":", subsets)