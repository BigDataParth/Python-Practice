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

# arr= [5, 2, 9, 1, 5, 6]

# #sorting_buble_sort
# def bub_sort(arr):
#     n=len(arr)
#     for i in range(n-2,0,-1):
#         for j in range(0,i+1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
# print(bub_sort(arr))  # Output: [1, 2, 5, 5, 6, 9]
 # Output: [1, 2, 5, 5, 6, 9]


 # Merge Sort
# arr = [3,4,2,1,4,7,2,8,34,23,11,32,12,13,14,15,16,17,18,19,20]

# def merge_array(left, right):
#     merged = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1
#     merged.extend(left[i:])
#     merged.extend(right[j:])
#     return merged


# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     mid = len(arr) // 2
#     left_half = merge_sort(arr[:mid])
#     right_half = merge_sort(arr[mid:])
#     return merge_array(left_half, right_half)

# print(merge_sort(arr))


#Quick sort
nums =[3,2,5,9,6,4,2,15,23,27,30,2,4,5]

def partition(nums,low,high):
    pivot=nums[low]
    i=low
    j=high
    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1
        while nums[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j

def quick_sort(nums, low, high):
    if low<high:
        p_index = partition(nums, low, high)
        quick_sort(nums, low, p_index - 1)
        quick_sort(nums, p_index + 1, high)
quick_sort(nums, 0, len(nums) - 1)
print(nums)  # Output: [2, 2, 3, 4,


