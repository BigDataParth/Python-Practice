# tup = (1,2,3,4,5)
# print(min(tup))

# a=[1, 2, 3]

# res =[(n,n**3) for n in a]

# print(res)

# import math

# a =(1,2,3,4,5)
# print(math.prod(a))

# test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]
# cus_eles = [6, 7, 8]

# a = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]

# ele = 4

# res =[tuple(j + ele for j in i) for i in a]

# print(res)


# # input
# tuple1 = (4, 5)
# tuple2 = (7, 8)

# # initialize an empty list to store the filtered tuples
# filtered_tuples = []

# # iterate over each element in tuple 1
# for element1 in tuple1:
# 	# iterate over each element in tuple 2
# 	for element2 in tuple2:
# 		# append a tuple of the two elements to the filtered list
# 		filtered_tuples.append((element1, element2))
# 		# append a tuple of the two elements in reverse order to the filtered list
# 		filtered_tuples.append((element2, element1))

# # output
# print(filtered_tuples)

# test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
# k=2
# res=[x for x in test_list if len(x) == k]

# print(res)

# a = [(1, 3), (4, 1), (2, 2)] 

# res= [sorted(a,key=lambda x: x[1])]
# print(res)

# test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)
# res ={x: test_tup.count(x) for x in test_tup}
# print(res)

# test_list = [(6, 24, 12), (7, 9, 6), (12, 18, 21)]

# res =[x for x in test_list if (i % 6 == 0 for i in x)]
# print(res)

# test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)] 

# res = [x for x in test_list if all(i > 0 for i in x)]
# print(res)

# test_tup = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])
# res=()
# for i in test_tup:
#     if i not in res:
#         res += (i,)
# print(res)

test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]


