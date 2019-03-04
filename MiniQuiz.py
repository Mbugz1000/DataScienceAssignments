def adder(value, list):
    list = list+[value]
    return list.index(value)

list = [1,2,4]

print(adder(5, list))
print(list)

import pandas as pd
df = pd.read_csv("C:\\Users\\ktmbugua\\Documents\\Digital Academy\\Data  Science\\Government_Appointments_to_State_Parastatal_Agencies.csv")
op = df.iloc[[11]]

print(df.columns.values)

def manip(key, val, dictionary):
    dictionary[key]=val
    return dictionary

print(manip('3','93',{}))

def print_names(people):
    """ A function to print a list of people's names. The parameter
        'people' is a list of people, where each person is represented
        as a list of their names.
    """
    count = 0
    num = len(people)-1
    while count <= num:
        name = people[count]
        num2 = len(name)-1
        count2 = 0
        wto_print = ""

        while count2 <= num2:
            wto_print += name[count2] + " "
            count2 += 1
        count += 1
        print(wto_print)

print_names(['Jesse', 'Ronald', 'Kumar'])

# names = input("Enter Your name")
# print("Welcome to Safaricom digital factory\n" + names+".")

def sqrs_to_n(n):
    for i in range(1, n+1):
        print(i, '*', i, '=', str(i*i))

print(sqrs_to_n(5))

def run_length_encode(list):
    to_print = []
    check = []
    for i in list:
        reps = list.count(i)
        if i not in check:
            check += [i]
            tup = (i, reps)
            to_print += [tup]

    print(to_print)

run_length_encode([10, 20, 30, 30, 30, 30])

def sqr(n):
    return n * n

print(sqr(-3))

# Assisting Bondo
df = pd.read_csv("C:\\Users\\ktmbugua\\Documents\\Digital Academy\\Data  Science\\Kisumu-County-Livestock-Distribution.csv")
df['Years'] = df.Date.str[-4:]
df.groupby(['Livestock', 'Years'])['Population'].sum().unstack().sort_values('2012' ,ascending=False).plot.bar()