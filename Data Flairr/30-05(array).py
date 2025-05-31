import array as arr

# ar =arr.array('b',[1,2,3,4,5,-20,-40,23])

# for i in ar:
#     print(i)

a =arr.array('i',[])

n=int(input('enter limit: '))

for i in range(n):
    x =int(input())
    a.append(x)
print(a)