# def display():
#     print('start')

# print('end')

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def reverse(s):
    n=0
    while s!=0:
        r= s%10
        s = s*10 + r
        n= n//10

    print(s)
