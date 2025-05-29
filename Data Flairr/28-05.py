# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
    
# def fact1(n):
#     f=1
#     while n!=0:
#         f*=n
#         n-=1
#     return f

# print(fact(5))  # Output: 120
# print(fact1(5))  # Output: 120

#lambda

# a=30
# b=30

# f =lambda a,b:a*b
# grat = lambda a,b: a if a>b b elif b>a
# print(grat(a,b))

def even_odd(n):
    if(n%2==0):
        return True
    else:
        False

my_list = [3,4,5,6,3,3,4,5,2,2,45,5,6,7,755,4,4333,34443,4]

a = list(filter(even_odd,my_list))

print(a)

