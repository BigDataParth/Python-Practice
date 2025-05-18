# test_list = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)] 

# sorted_list = sorted(test_list, key=lambda x: (x[0], x[1]), reverse=True)
# print(sorted_list)


# test_tup = (1, 5, 7, (4, 6), 10)
# temp_list =list(test_tup)
# for i in temp_list:
#     if isinstance(i, tuple):
#         temp_list.remove(i)
# print(tuple(temp_list))
        
test_tuple = (5, (6, (7, 8, 6)))

# def flatten(tup):
#     flat_list = []
#     for item in tup:
#         if isinstance(item, tuple):
#             flat_list.extend(flatten(item))
#         else:
#             flat_list.append(item)
#     return flat_list
# flat_list = flatten(test_tuple)

# res= {X: flat_list.count(X) for X in flat_list}
# print(res)

# test_list = [(3, 4, 5), (4, 5, 7), (1, 4)]
# res=[]
# for i in test_list:
#     for j in i:
#         res.append(j)
# print(list(set(res)))

# test_tup1 = (3, 4),
# test_tup2 = (5, 6),

# from collections import Counter

# test_list = [(6, 5), (1, 7), (2, 5), (8, 7), (9, 8), (3, 7)] 

# freq = Counter(j for i,j in test_list)

# print(freq)

# res = sorted(test_list, key=lambda x: freq[x[1]], reverse=True)
# print(res)

# test_tup = ([7, 5, 4], [8, 2, 4], [0, 7, 5])
# res = [sorted(i) for i in test_tup]
# print(tuple(res))



# test_list = [('Gfg', 10), ('best', 3), ('CS', 8), ('Geeks', 7)]

# ord_list = ['Geeks', 'best', 'CS', 'Gfg'] 

# res =sorted(test_list,key=lambda x: ord_list.index(x))
# print(res)

# test_list1 = [(3, 4), (5, 6)]
# test_list2 = [(5, 4), (4, 3)] 

# for i in test_list1:
#     for j in test_list2:
#     print(sorted(i))
       