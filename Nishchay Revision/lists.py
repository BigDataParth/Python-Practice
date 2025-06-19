# list1 = [1, 2, 3, 4, 5]
# a = list1[0]  # Accessing the first element of the list
# list1[0]=list1[-1]
# list1[-1] = a  # Swapping the first and last elements
# print(list1)  # Output: [5, 2, 3, 4


#swap elements in list
# Revering a list

# list1 = [1, 2, 3, 4, 5]
# list1.reverse()  # This will reverse the list in place
# print(list1)  # Output: [5, 4, 3, 2, 1]

# remove multiple elements from the list
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# elements_to_remove = [2, 4, 6, 8]
# list2= [i for i in list2 if i not in elements_to_remove]
# print(list2)  # Output: [1, 3, 5, 7, 9]

#break a list into chunks
# lst =[1, 2, 3, 4, 5, 6, 7, 8, 9]
# chunk_size=3

# for i in range(0, len(lst), chunk_size):
#     print(lst[i:i + chunk_size])

# #EVEN NUMBERS IN A LIST
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_numbers = [i for i in lst if i % 2 == 0]
# print(even_numbers)  # Output: [2, 4, 6, 8]

# # ODD
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# odd_num =[i for i in lst if i%2==1]
# print(odd_num)  # Output: [1, 3, 5, 7, 9]

# print positive and negative numbers in a list
# lst = [1, -2, 3, -4, 5, -6]
# positive_numbers = [i for i in lst if i > 0]
# negative_numbers = [i for i in lst if i < 0]
# print(positive_numbers)  # Output: [1, 3, 5]
# print(negative_numbers)  # Output: [-2, -4, -6]

# finding second smallest number in a list
# lst = [5, 2, 8, 1, 4]
# lst.sort()
# second_smallest = lst[1]
# print(second_smallest)  # Output: 2

# # counting occurrences of an element in a list
# lst = [1, 2, 3, 1, 2, 1, 4]
# import collections
# count = collections.Counter(lst)
# print(count)  # Output: Counter({1: 3, 2: 2, 3: 1, 4: 1})


# Duplicate removal from a list
# lst = [1, 2, 3, 1, 2, 4]
# unique_lst = list(set(lst))   
# print(unique_lst)  # Output: [1, 2, 3, 4]

#sum of elements in list

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sum(list))  # Output: 45

#common elelments in two lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# list3 = list(set(list1) & set(list2))
# print(list3)  # Output: [4, 5]

#slit list into two halves
# lst = [1, 2, 3, 4, 5,6,7,8,9,10]
# mid =len(lst) // 2
# first_half = lst[:mid]
# second_half = lst[mid:] 
# print("First half:", first_half)  # Output: [1, 2, 3, 4, 5]
# print("Second half:", second_half)  # Output: [6, 7,

# # getting digits from list
# lst=[1,2,3,'a','b',4,5,6]
# gig =[i for i in lst if isinstance(i, int)]
# print(gig)  # Output: [1, 2, 3, 4, 5, 6]

# # getting letters from list
# lst=[1,2,3,'a','b',4,5,6]
# letters = [i for i in lst if isinstance(i, str)]
# print(letters)  # Output: ['a', 'b']

# cumulative sum of a list
# lst = [1, 2, 3, 4, 5]
# cumsum=[]
# total=0
# for i in lst:
#     total += i
#     cumsum.append(total)
# print(cumsum)  # Output: [1, 3, 6, 10, 15]


# lst = ['oak', 'banana', 'apple', 'orange', 'grape','as']
# nlst=[i for i in lst if len(i)%2==0]
# print(nlst)  # Output: ['banana', 'orange', 'grape']

#removingempty strings

# lst = [1,2,3,'parth','','bhav','']
# nlst =[i for i in lst if i!='']
# print(nlst)  # Output: [1, 2, 3, 'parth', 'bhav']

# #get indices of elements in a list
# lst = [1, 2, 3, 4, 5]
# indices = [i for i, x in enumerate(lst) if x % 2 == 0]
# print(indices) 

# to convert a list ofcharacters to a string
# lst = ['h', 'e', 'l', 'l', 'o']
# print(''.join(lst))  # This will concatenate the characters into a string

# list of tuples into a list of strings
# lst = [('a', 1), ('b', 2), ('c', 3)]
# nlst =[i for i,j in lst ]

#pairwise sum of elements in a list
# lst = [1, 2, 3, 4, 5]
# pairwise_sum = [lst[i] + lst[i + 1] for i in range(len(lst) - 1)]
# print(pairwise_sum)  # Output: [3, 5, 7, 9]


# maximum product of two elements in a list
# lst = [1, 2, 3, 4, 5]
# sortlst = sorted(lst, reverse=True)  # Sort the list in descending order
# max_product = sortlst[0] * sortlst[1] 
# # Multiply the two
# print(max_product)  # Output: 20


#palindrome check in a list
lst = ['a', 'b', 'c', 'b', 'a']
is_palindrome = lst == lst[::-1]
print(is_palindrome)  # Output: True
