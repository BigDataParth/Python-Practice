# lambada and filter 
# mylist =[19,44,56,3,44,77,87,65,64]

# mylist1 =filter(lambda x:x%2==0,mylist)

# print(list(mylist1))

# my_string = 'Parth Kiran Bhavthankar'

# lis =filter(lambda x:x in ('a','e','i','o','u'),my_string.lower())

# print(list(lis))

# Lambda With Map
# my_list = [1,2,3,5,7,8,5,9]

# lis = map(lambda x :x*x,my_list)

# def fact(n):
#     f=1
#     while(n!=0):
#         f = f*n
#         n =n-1
#     return f

# print(fact(5))

# def fact(n):
#     if n==0 or n==1 :
#         return 1
#     else:
#         return n * fact(n-1)
    
# print(fact(5))

# print(list(lis))

import functools as ft

# def myfunc(a,b):
#     return a+b

# mylis =[2,4,3,5,6]

# p = ft.reduce(myfunc,mylis)
# print(p)

lis =[1,66,43,23,22,42,68]

p =ft.reduce(lambda a,b:a+b,lis)

print(p)