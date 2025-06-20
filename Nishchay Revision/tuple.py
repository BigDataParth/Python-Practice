tuple1 =(1, 2, 3, 4, 5)
# print(len(tuple1))  # Output: 5
# print(sum(tuple1))  # Output: 15
# print(max(tuple1))  # Output: 5
# print(min(tuple1))  # Output: 1
# print(tuple1.count(3))  # Output: 1
# print(tuple1.index(4))  # Output: 3
# x=1
# for i in tuple1:
   
#     x = x*i
# print(x)

# list =[(1, 2), (3, 4), (5, 6)]
# dict = {i: j for i, j in list}
# print(dict)


# list =[(1,2,3,4,5),(1,2,3),(1,2,3,4,5,6)]
# dict = {i: j for i, j in enumerate(list)}
# print(dict)  

# list =[(1,2,3,4,5),(1,2,3),(1,2,3,4,5,6)]
# for i in list:
#     for j in i:
#         print(j, end=' ')
#     print()  # Print a new line after each tuple

# list =[(1,2,3,4,5),(1,2,3),(1,2,3,4,5,6)]
# nlist=[i for i in list if len(i)>3]
# print(nlist)

#removes tuples having every element none
# list =[(1,2,3,4,5),(None,None,None),(1,2,3,4,5,6)]
# nlist =[i for i in list if all(x is not None for x in i)]
# print(nlist)


# list =[('parth', 1), ('bhav', 2), ('nishchay', 3)]
# list.sort(key=lambda x: x[0] )
# print(list)  # Sort by the second element of each tuple0

#sort list of tuples by total digits
# list =[(1,2,3,4,5),(1,2,3),(1,2,3,4,5,6)]
# list.sort(key=lambda x: sum(len(str(i)) for i in x))
# print(list)

# tuple = (1, 2, 3, 4, 5)
# list1 =list(tuple)  # Convert tuple to list
# print(list1)  # Output: [1, 2, 3, 4, 5]

# Element frequency in a tuple
# tuple1 = (1, 2, 3, 1, 2, 4, 1)
# from collections import Counter   
# count = Counter(tuple1)
# print(count)  # Output: Counter({1: 3, 2:

# cross pairing of tuples
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# cross_pairs = [(a, b) for a in tuple1 for b in tuple2
#                if a != b]  # Exclude pairs where elements are equal
# print(cross_pairs)  # Output: [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
# tuple= (1, 2, 3, 4, 5)
# tuple2 = (6, 7, 8, 9, 10)
# cros= [(a,b,c) for a in tuple for c in tuple2 for b in tuple if a != b!= c]
# print(len(cros))  # Output: 15


x=[]
list = [(1, 2), (3, 4), (5, 6)]
for i in list:
    for j in i:
        x.append(j)
print(tuple(x) )