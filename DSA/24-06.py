#palindrome
# str ='mpm'
# def is_palindrome(s):
#     if s==s[::-1]:
#         return True
#     else:
#         return False

# print(is_palindrome(str))  # Output: True
# WIth Recursion
# str ='abcdef'
# def is_palindrome(s,Left,Right):
#     if Left >= Right:
#         return True
#     if s[Left] != s[Right]:
#         return False
#     return is_palindrome(s, Left + 1, Right - 1)
# print(is_palindrome(str, 0, len(str) - 1))  # Output: True

# lst =[0,1]
# for i in range(2, 10):
#     lst.append(lst[i-1] + lst[i-2])
# print(lst)  # Output: [0, 1, 1, 2,


# #Sorting
# nums =[5, 2, 9, 1, 5, 6]
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] > arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr
# print(selection_sort(nums))  # Output: [1, 2, 5, 5, 6, 9]

arr= [5, 2, 9, 1, 5, 6]

#sorting_buble_sort
def bub_sort(arr):
    n=len(arr)
    for i in range(n-2,0,-1):
        for j in range(0,i+1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bub_sort(arr))  # Output: [1, 2, 5, 5, 6, 9]
 # Output: [1, 2, 5, 5, 6, 9]