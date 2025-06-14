import numpy as np

myar = np.array([[1, 50 , 30], [4, 5,8],[1,2,3]])
mt1 = np.matrix(myar)
mt2 =np.matrix('1 2 3; 4 5 6; 7 8 9')
# print(mt1.min())
# print(mt1.max())
# print(mt1.transpose())
# print(mt1.diagonal())
# print(mt1.trace())
# print(mt1.lower())

# Runtime Append

# import array as ar
# m,n = [int(a) for a in input('Number of rows and columns: ').split()]
# x =m*n
# myar11 = ar.array('i', [])
# for i in range(x):
#     a = int(input('Enter element: '))
#     myar11.append(a)

# myar12 =np.reshape(myar11, (m, n))
# mt3 = np.matrix(myar12)
# print(mt3)


# uper and lower triangular matrix

m,n = [int(a) for a in input('Number of rows and columns: ').split()]
x =m*n
mytr = np.array('i', [])
for i in range(x):
    a = int(input('Enter element: '))
    mytr = np.append(mytr, a)
mytr2 = np.reshape(mytr, (m, n))
mt4 = np.matrix(mytr2)

for r in range(m):
    for c in range(n):
        if r >= c:
            mt4[r, c] = 0  # Lower triangular matrix
        elif r <= c:
            mt4[r, c] = 0  # Upper triangular matrix
print("Lower Triangular Matrix:")
print(mt4)