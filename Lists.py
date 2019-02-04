import numpy as np
# Lists class

# fruits = list(('Apple', 'Banana', 'Carrot', 'Tomato', 'Treetomato'))
# no = 0
# for x in enumerate(fruits):
#     print(x)

x = [1, 2, 3, 4]
y = [5, 6, 7, 8, 9]
y1 = x+y

# Using list comprehension to raise it to ^3
z = [y1**3 for y1 in y1]
# print(z)

a = [[1, 2], ['Kaka', 'Dida'], [10, 12]]
# print(a[2][1])

b = np.array([1, 2, 3, 4, 5])
# print(b)

c = np.array([[2, 1],
              [1, 0]])

d = np.array([[4],
              [1]])

print(c.dot(d), d.shape)
