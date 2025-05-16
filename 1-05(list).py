l1 = [[],1,2,3,4,5,6]
# l2 =[]
# for i in l1:
#     if i:
#         l2.append(i)
# print(l2)

# test_list = [[4, 5, 6], [5, 6, 4, 1], [4], [4, 8, 9, 10]]

# N=4

# res=[]

# for i in test_list:
#     if N in i:
#         i.remove(N)
#         res.append(i)
# print(res)

# a = [10, 20, 30, 40, 50, 60, 70]

# remove = [20, 40, 60]

# res = []

# for i in remove:
#     if i in a:
#         a.remove(i)
        
# print(a)

# x = ["hello", "world", "hi", "hello world"]
# cnt =0
# for i in x:
#     if 'hello' in i:
#         cnt+=1
# print(cnt)

a = ['GeeksforGeeks', 'is', 'Best', 'For', 'Geeks', 'And', 'Computer Science']

# list of word replacements 
b = [['Geeks', 'Gks'], ['And', '&'], ['Computer', 'Comp']]

# replace_map = dict(b) # convert `b` to dictionary

# for key, val in replace_map.items():
#     a = [ele.replace(key, val) for ele in a]

# print(a)


# input_list = [1, 2, 2, 5, 8, 4, 4, 8]

# print(len(set(input_list)))

# test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# K = 3 
# res=[]
# for i in test_list:
#     if test_list.count(i) >= K:
#         res.append(i)
# print(set(res))


# a = [1, 2, 1, 2, 3, 4, 5]

# for i in range(len(a) - 2):
#     if a[i] == a[i + 1] == a[i + 2]:
#         print("Found")
#         break
# else:
#     print("Not Found")


# from itertools import permutations

# a = [1, 2, 3]
# for combo in permutations(a, 3):
#     print(combo)

    
