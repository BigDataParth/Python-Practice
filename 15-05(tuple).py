t = ('A', 'B', 'C')

# res= tuple((t[i], t[i+1]) for i in range(len(t)-1))
# print(res)

# test_list = [['Best'], ['Gfg'], ['Gfg']] 
# # res=tuple()
# # for i in test_list:
# #     for j in i:
# #         t=res.append(tuple((j,)))
# # print(t)

# res=tuple(tuple(i,) for i in test_list)
# print(res)

# test_list = [[4, 5], [7, 3]]
# add_list = ['Gfg', 'best']

# res=[]

# for i,j in zip(add_list, test_list):
#     for k in j:
#         res.append((i, k))
# print(res)


# a = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
# b=['key','value','id']
# # res=[]
# # for i,j in zip(b, a):
# #     for k in j:
# #         res.append(i,k)
# # print(res) 

# res= [{'key':i[0], 'value':i[1], 'id':i[2]} for i in a]
# print(res)


# test_tup = (4, 56) 

# res ='.'.join(map(str, test_tup))
# print(res)

# test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]
# K = 2
# res=[sub for sub in test_list if all(j > 9 and j < 100 for j in sub)]
# print(res)

        
test_list = [(6, 7), (2, 3), (7, 6)] 
res =[]
tes=[]
for i in test_list:
    res.append(sorted(i))
print(res)
for j in res:
    if j in tes:
        continue
    else:
        tes.append(j)

# res = [i for i in test_list if i[0] > 5 and i[1] > 5


