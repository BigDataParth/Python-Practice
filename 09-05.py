# Dictionary COnversion

a = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# res=[[key,value] for key,value in a.items()]
# print(res)

a = ["name", "age", "city"]  
b = [["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"], ["Charlie", 22, "Chicago"]]



# res=[dict(zip(a,v)) for v in b]

# print(res)

# a = [["a", 1], ["b", 2], ["c", 3]]

# print(dict(a))

# a = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]

# res = {d['name']: d['age'] for d in a}
# print(res)


# a = [("name", "Alice"), ("age", 25), ("city", "New York")]
# print(dict(a))



# a = [("a", 1), ("b", 2), ("c", 3)]

# res = dict(a)

# print(res)

from collections import defaultdict

d = {'gfg': {'x': 5, 'y': 6}, 'is': {'x': 1, 'y': 4}, 'best': {'x': 8, 'y': 3}}
res = defaultdict(tuple)
# for key, value in d.items():
#     for k, v in value.items():
#         res[k] += (v,)
# print(str(list(res.items())))

print(d.items())