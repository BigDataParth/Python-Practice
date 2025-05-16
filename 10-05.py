a = {'Gfg': 4, 'is': 5, 'best': 9}
b = [8, 3, 2]

# res ={key:{k:value} for key,(k,value) in zip(b,a.items())}
# print(res)

# test_dict = {'Gfg': { 'a' : [1, 3], 'b' : [3, 6], 'c' : [6, 7, 8]},
#              'Best': { 'a' : [7, 9], 'b' : [5, 3, 2], 'd' : [0, 1, 0]}}
# res=dict()
# for key, value in test_dict.items():
#     for k, v in value.items():
#         if k not in res:
#             res[k] = []
#         res[k].extend(v)
# print(res)


# from collections import OrderedDict
# d = {'gfg' : 4, 'is' : 2, 'best' : 5}
# print(str(d))

# print(OrderedDict(reversed(list(d.items()))))

# a = ["Gfg", "is", "Good", "for", "Geeks"]
# d = {"ab": 5, "Best": 6}
# K = "Gfg"

# if K in a and K in d.keys():
#     print("Yes")
# else:
#     print("No")


# d = {'name1': 'hello world', 'name2': 'python code', 'name3': 'world peace'}
# substring = 'world'

# for k,v in d.items():
#     if substring in v:
#         for k in 

# test_list = [{"gfg": 2, "best" : 4},  
#              {"gfg": 2, "is" : 3, "best" : 4},  
#              {"gfg": 2}] 

# res = max(test_list, key = lambda x: len(x))
# print(res)    

# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]

# res  = dict(zip(keys,values))
# print(res)
# a=[]
# test_dict = {'gfg': [5, 6, 7, 8],
#              'is': [10, 11, 7, 5],
#              'best': [6, 12, 10, 8],
#              'for': [1, 2, 5]}

# for key, value in test_dict.items():
#     for i in value:
#         if i not in a:
#             a.append(i)
# print(sorted(a))

# test_dict = {'gfg' : [1, 2, 3], 'is' : [1, 4], 'best' : [4, 2]} 

# res ={}

# for key, value in test_dict.items():
#     for i in value:
#         if i in res:
#             res[i].append(key)
#         else:
#             res[i] = [key]
# print(res)

# dict = {} # initialize empty dictionary
# temp=0
# a = ['bat', 'nat', 'tan', 'ate', 'eat', 'tea']

# for word in a:
#     sorted_word = ''.join(sorted(word)) # sort the letters in the word
#     if sorted_word in dict:
#         dict[sorted_word].append(word) # add the word to the list of anagrams
#     else:
#         dict[sorted_word] = [word] # create a new list for the anagram group

# b =list(dict.values()) # get the list of anagram groups


# for i in b:
#     if len(i)>temp:
#         temp = len(i)
# print(temp) # print the length of the largest anagram group


# a = ['bat', 'nat', 'tan', 'ate', 'eat', 'tea']

# for word in a:
#     sorted_word = ''.join(sorted(word))
#     print(sorted_word)

# test_dict = {'Gfg' : [6, 7, 4], 'is' : [4, 3, 2], 'best' : [7, 6, 5]} 

# res = {value:sum(value) for key,value in test_dict.items()}
# print(res)

test_dict = {'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
             'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
             'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}}

res = {key : dict(sorted(value.items(), key = lambda x:x[1])) for key, value in test_dict.items()}
print(res)