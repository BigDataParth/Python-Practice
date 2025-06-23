

#armstrong number
# def is_armstrong(num):
#     sum=0
#     nod =len(str(num) )
#     temp=num
#     while temp>0:
#         digit = temp % 10
#         sum += digit ** nod
#         temp //= 10
#     return sum
# if is_armstrong(num) == num:
#     print(f"{num} is an Armstrong number")


# print factors of given number give list of it

num=64
from math import sqrt

# def factors(num):
#     factor_list = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             factor_list.append(i)
#     return factor_list

# print(factors(num))

# result=[]

# for i in range(1, int(sqrt(num)) + 1):
#     if num % i == 0:
#         result.append(i)
#         result.append(num // i)
# result = list(set(result))  # Remove duplicates
# result.sort()  # Sort the factors
# print(result)


# HASHING

n=[1,2,3,3,45,4,3,2,3,6,7,8,2,1,7,8,9,3,2,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
m=[10,111,2,3,4,9,2]
num=3
# frequency of elements in a list
enumerate_dict = {}
for i in n:
    if i in enumerate_dict:
        enumerate_dict[i] += 1
    else:
        enumerate_dict[i] = 1

print(enumerate_dict[num])

