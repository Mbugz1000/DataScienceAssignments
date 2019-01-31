import numpy as i
some_list = [1, 2, 3, 5, 7, 9]

mylist = []

for i in some_list:
    if not i.isnan():
        mylist.append(i)

#List Comprehension
#myList2=[i for ]