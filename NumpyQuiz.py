import numpy as np
some_list = [1, 2, 3, 5, 7, 9]
#
mylist = []

for i in some_list:
    if not np.isnan(i):
        mylist.append(i)

# List Comprehension
myList2 = [i for i in mylist if not np.isnan(i)]
print(myList2)

print(np.version.version)