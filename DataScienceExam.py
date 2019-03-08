import pandas as pd
import numpy as np
results = "Dwards: 70 %, Thanasius: 40 %, Alvin: 80 %, Uther: 48 %, Purgeon: 97 %"

def splitter(astring):
    namesresult = c.split(",")
    data = [x.split(":") for x in namesresult]
    df = pd.DataFrame(np.array(data), columns=['name', 'marks'])
    df['status'] = np.where(df.marks.astype(int) > 49, 'Pass', 'Fail')
    return df

# print(splitter(results))

import math

def qdr(a, b, c):
    return (-b+math.sqrt(b**2-4*a*c))/2*a

print(qdr(1, -4, 3))

def r2(n):
    return [x for x in range(1, n*2, 2)]

import pandas as pd

print(r2(5))

df = pd.read_csv("C:\\Users\\ktmbugua\\Documents\\Digital Academy\\Data  Science\\Employee_churn.csv")

df['Department'] = df.Department.str.upper()
sales = df.Department.str.contains('(?i)_sales')
support = df.Department.str.contains('(?i)support.|support?')
technical = df.Department.str.contains('(?i)technical.')
df['Department'] = np.where(sales, 'SALES', np.where(support, 'SUPPORT', np.where(technical, 'TECHNICAL', df['Department'])))
df2 = df.rename(index=str, columns={"satisfaction_level":"Employee count"})
departments = df2.groupby('Department').count()["Employee count"].reset_index()


# print(departments[departments["Department"]=="SALES"].values)
import matplotlib.pyplot as plt

df.groupby('salary').satisfaction_level.mean().sort_values(ascending=False).plot.bar()
plt.title('Salary Level vs Average Satisfaction Level', fontsize=16, fontweight='bold')
plt.xticks(rotation=0)

female = df['Gender '].str.contains('F')
df['Gender '] = np.where(female, 'Female', df['Gender '])
df.groupby('Gender ').average_montly_hours.mean().sort_values(ascending=False).plot.bar()
plt.title('Gender vs Average Monthly Hours Worked', fontsize=16, fontweight='bold')
plt.xticks(rotation=0)

sales = df.Department.str.contains('(?i)_sales|sales')
df['Department'] = np.where(sales, 'Sales', df['Department'])

df[df.Department == 'Sales'].plot.hexbin(x='satisfaction_level', y='number_project', gridsize=25)


# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(df2[['satisfaction_level']], df2[['number_project']], random_state=0)
# linreg = LinearRegression()
# linreg.fit(X_train, y_train)
#
# df2.plot.scatter(y='number_project', x='satisfaction_level', marker='o')
# plt.plot(df2['satisfaction_level'], linreg.coef_*df2['satisfaction_level']+linreg.intercept_, 'r-')