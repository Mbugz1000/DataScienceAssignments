# Pandas 2

import pandas as pd

# import data

df = pd.read_csv("C:\\Users\\ktmbugua\\Documents\\Digital Academy\\Data  Science\\Government_Appointments_to_State_Parastatal_Agencies.csv")

def rest_of_code():
    print(df.head(10))
    print("\n", df.sample(5))

    print(df.describe())
    print(df.info())
    # No. of null values in the table
    print(df.isna().sum())

    # Referencing the columns
    print(df.columns[8])

    print(df.describe(include='all'))
    print(df.dtypes)

    # Using categorical data
    df['Gender'] = df['Gender'].astype('category')
    print(df['Gender'].dtype)

    df['End_Date'] = pd.to_datetime(df['End_Date'])
    print(df['End_Date'].dtype)

dates = ['Date_Appointed_', 'Start_Date', 'End_Date', 'Year']

for date in dates:
    df[date] = pd.to_datetime(df[date])

print(df.dtypes)

# List the frequency of positions
print(df['Position_'].value_counts())

# What is the time span of your data? e.g. (June 2018, June 2019)
print(df.describe(include='all'))  # Using min, max

#  Find the name of the person with the longest duration between Date of appointment and Start date
df['Duration_idle'] = df['Date_Appointed_'] - df['Start_Date']
# print(df.sample())
names = df[df['Duration_idle'] == df['Duration_idle'].max()].Persons_Appointed_
namesPosition = df[df['Duration_idle'] == df['Duration_idle'].max()][['Persons_Appointed_','Position_']]
print(names)

#  What is the std dev. of duration months?
print(df.describe(include='all'))  # Check std dev

# Group by position and Gender by count
positionGender = df.groupby(['Position_', 'Gender']).count()['GAZETTE_NOTICE_NO_']
print(positionGender)

# Find the number of appointments after 15th April 2015
greaterThan = df[df['Date_Appointed_']>"2015-04-15"].count()['GAZETTE_NOTICE_NO_']
print(greaterThan)
