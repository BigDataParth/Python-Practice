# s = "Python is Fun!"
# v = "aeiouAEIOU"

# for i in s:
#     if i in v:
#         print(i,s.count(i), end='\n')

# lst =["banana", "apple", "cherry", "date"]

# lst.sort(reverse=True)
# print(lst)
# lst.sort()
# print(lst)
# from datetime import datetime
# dates = ["24 Jul 2017", "26 Jul 2017", "25 Jul 2017", "27 Jul 2017", "28 Jul 2017"]

# dates.sort(key=lambda x: datetime.strptime(x, "%d %b %Y"))
# print(dates)

# s = "Python is Fun!"
# print(s.center(21, '*'))

# s ='21/05/1995'
str = "Geeksforgeeks"
n=3
res=[]
for i in range(0, len(str)+3, n):
    res.append(str[i:i+n])
print(res[0:len(res)-1])