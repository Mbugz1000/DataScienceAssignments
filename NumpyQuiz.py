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

# 20
import csv
file = open('C:\\Users\\ktmbugua\\Documents\\Digital Academy\\Data  Science\\emp_salo.csv')
empSalaries = np.genfromtxt(('\t'.join(item) for item in csv.reader(file)),
                            delimiter='\t', dtype=str)

print(empSalaries.shape)

# 21
removedSalBlanks = np.array([sal for sal in empSalaries[1:] if not sal[4] == ''])
floatSalary = [float(sal) for sal in removedSalBlanks[0:, 4]]

print('\nJob Title with max Salary is', removedSalBlanks[np.argmax(floatSalary), 0])

# 22
print('\nTotal salary paid is', np.sum(floatSalary))

# 23
difference = np.max(floatSalary) - np.min(floatSalary)
print('\nThe difference between the highest and the lowest salary is', difference, '. Lowest job is',
      removedSalBlanks[np.argmin(floatSalary), 0])

# 24
print('\nSorted by the Job Description\n', removedSalBlanks[np.argsort(removedSalBlanks[:, 0])])

# 25
print('\nNo. of Departments are', len(set(removedSalBlanks[:, 1])))

# 26
import datetime as dt
removedDayBlanks = np.array([day for day in empSalaries[1:] if not day[3] == ''])
dateHire = [dt.datetime.strptime(day[0:10], '%m/%d/%Y') for day in removedDayBlanks[0:, 3]]
print('\nJob Title and Salary of longest serving employee is', removedDayBlanks[np.argmin(dateHire), (0, 4)], 'respectively')


# 27
deptNames = np.sort(list(set(removedSalBlanks[:, 2])))
def deptsalsum(deptname):
    return np.sum([float(deptSal[1]) for deptSal in removedSalBlanks[:, (2, 4)] if deptSal[0] == deptname])

sums = np.array([deptsalsum(deptname) for deptname in deptNames])
print('\nSalaries each department gives out\n', np.concatenate((np.array(sums[:, None]),
                                                              np.array(deptNames[:, None])), axis=1))

# 29
dateset = np.array(list(set(dateHire)))
jobs = ['']
dateNo = 0
while True:
    if len(jobs) < 2:
        jobs = [removedSalBlanks[dates[0], 0] for dates in enumerate(dateHire) if dates[1] == dateset[dateNo]]
        dateNo += 1
    else:
        break

print('\nThese Job Title were hired on the same day\n', jobs)
