# 1
import numpy as np
some_list = [1, 2, 3, 5, 7, 9]

mylist = []

for i in some_list:
    if not np.isnan(i):
        mylist.append(i)

# List Comprehension
myList2 = [i for i in mylist if not np.isnan(i)]
# print(myList2)

# 2
print(np.version.version)

# 4
zeros = np.zeros((1000,), dtype=int)
# 5
zeros[500] = 7
# print(zeros)

# 6
# print(np.random.rand(5, 5))


# 8
def datatype(item):
    return type(item)

# print(datatype(2))

# 10
test=[1, 'a']
testtype = datatype(test)
# print(np.array(test, testtype))

# 13
twod= np.array([[1, 2],
                [3, 4]])

# 14
# print(twod, twod.shape)

# 15
oned = twod.flatten()
# print(oned)

# 16
xarr = np.arange(10)
# print(xarr[0:2], xarr[2:], xarr[::-1])

# 17
# print(xarr.reshape((2, 5), order='C'))

# 18
a = np.array([14, 15, 16, 17, 18, 19], dtype='float32')
b = np.array([4.5, 4, 4, 2, 5.6])
# print(np.concatenate((a, b)))

# 19
