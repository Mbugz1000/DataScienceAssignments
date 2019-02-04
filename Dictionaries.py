# Class for Dictionaries and Pandas
# Dictionaries
names = ['John', 'Peter', 'Simon', 'Jane', 'June']
grades = [67, 38, 95, 22, 45]

safcom = {'names': names}
safcom2 = {'grades': grades}
safcom.update(safcom2)
print(safcom['names'][1], ':', safcom['grades'][1], '\n')

for n, g in zip(grades, names):
    print(n, g)

# Pandas
import pandas as pd

df = pd.DataFrame({'names': names, 'grades': grades})
print('\nNames:\n', df.names)

print('\nMax grade:\n', df['grades'].max())

english = [45, 56, 67, 78, 89]
names = ['John', 'Mark', 'Andrew', 'Jane', 'Alice']

df = pd.DataFrame({'names': names, 'english': english})
df['math'] = [87, 98, 78, 88, 77]
print('\n', df)

# Column calculations
print(df.info(), '\n', df.describe())
df['science'] = (df['math'] + df['english'])/2
df['cre'] = df[['science', 'english']].min(axis=1)
df['social_studies'] = df[['math', 'english', 'science']].max(axis=1)
df['total'] = df[['math', 'english', 'science', 'social_studies', 'cre']].sum(axis=1)
print('\n', df)
# Create a Dictionary with grades, divide by 5 then create a new column with student grades
