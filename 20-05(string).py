s= 'geeksforgeeks is best for geeks'
w= 'for'

# res =s.find(w)

# if res ==-1:
#     pos=-1
# else:
#     pos =s[:res].count(' ') + 1

# print(pos)

# res =s.split().index(w) +1
# print(res)

# s = "aaabbccaaaa"
# set1=set(s)
# res = {i:s.count(i) for i in set1}
# print(res)

# test_list = [4, 7, 8, 3, 2, 1, 9]
# res=''
# for i in test_list:
#     res+=str(i)
#     res+='*'
# print(res[:-1])

# str = 'gfg, is, (best, for), geeks'
# res = str.split(',')
# print(res)

s = 'Geeksforgeeks is best for geeks and CS'
li = ["best", "CS", "for"]
k = "gfg"
res =''

for i in s.split():
    if i in li:
        s = s.replace(i, k)
    else:
        

