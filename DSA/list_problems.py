#Largest Elemenet in an Array
nums = [43,23,12,22,51,74,234,12,34,56,78,90,100,200,300,400,500]
        # largest=0
        # i=0
        # while i < len(arr):
        #     if arr[i] > largest:
        #         largest = arr[i]
        #     i += 1

        # print("Largest element in the array is:", largest)  # Output: 500

# finding second largest element in an array
# arr_sorted = sorted(arr, reverse=True)
# print("Second largest element in the array is:", arr_sorted[1])  # Output: 400

# n =len(arr)
# largest=float('-inf')
# s_largest=float('-inf')
# for i in range(n):
#     if arr[i] > largest:
#         s_largest = largest
#         largest = arr[i]
#     elif arr[i] > s_largest and arr[i] != largest:
#         s_largest = arr[i]
# print("Largest element in the array is:", largest)  # Output: 500
# print("Second largest element in the array is:", s_largest)  # Output:

n= len(nums)
for i in range(0,n-1):
    if nums[i]< nums[i+1]:
        print('sorted')
    else:
        print('not sorted')
        break


