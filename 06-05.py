dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = {4: 'd', 5: 'e', 6: 'f'}

# dict1.update(dict2)
# # print(dict1) # Merging dictionaries using the + operator (Python 3.9+)
# from collections import OrderedDict
# dict1.update({'manjeet':'3'})
# print(dict1) # Merging dictionaries using the update() method

# d = {"Gfg": [5, 7, 5, 4, 5], "is": [6, 7, 4, 3, 3], "Best": [9, 9, 6, 5, 5]}

# for key, value in d.items():
#     print(max(value), end=" ")

a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

# Create a list of unique items
b = list(set(a))

# Use list comprehension to count the frequency of each unique item
c = {item: a.count(item) for item in b}

# Print the frequency of each item
print(c)