import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

df = pd.read_csv("C:\\Users\\ktmbugua\\Documents\\Digital Academy\\Data  Science\\MiniProject\\CDF_Expenditure_on_Projects.csv")
df.drop(columns=['index_', 'remarks', 'prox2', 'district', 'constituency', 'location'], inplace=True)
activities = df['activity_to_bedone']
classroom = activities.str.contains('(?i)classroom')
latrines = activities.str.contains('(?i)latrines|toilet')
classroomLatrines = (classroom & latrines)
roadRepair = activities.str.contains('(?i)murram|road|grading')
dispensary = activities.str.contains('(?i)dispensary')
df['activity_to_bedone'] = np.where(roadRepair, 'Road Repair',
                                    np.where(classroom, 'Construction/Renovation of Classrooms',
                                             np.where(latrines, 'Construction of Latrines',
                                                      np.where(classroomLatrines, 'Construction/Renovation of Classrooms and Latrines',
                                                               np.where(dispensary, 'Construction of Dispensary',df['activity_to_bedone'])))))

implementation = df['implementation_status']
ongoing = implementation.str.contains('(?i)ongoing|on going|on-going|incomplete|on - going|going|in progress|50%|tendering|pending|ongoi|gpomg|still requires|plastering|painting|started')
notStarted = implementation.str.contains('(?i)not started|not yet started|new|stalled|to start|not yet|yet to begin|ye to commence|not stated|to comenc|to commence|to be started')
fundsReallocated = implementation.str.contains('(?i)allocated|allocation|rea located|realloca')
complete = implementation.str.contains('(?i)complete|done|purchased|roofed|coomplete|pipes laid|in use|rehebilitated|100%|repaired|coimplte|dug|rehabilitated|bed made|plastered|renovated|in place')
df['implementation_status'] = np.where(complete, 'Complete',
                                       np.where(ongoing, 'Ongoing',
                                                np.where(notStarted, 'Not Started',
                                                         np.where(fundsReallocated, 'Funds Re-allocated', 'Other'))))

expectedOutput = df['expected_output']
expClassrooms = expectedOutput.str.contains('(?i)class|facilities|edu|education')
expRoad = expectedOutput.str.contains('(?i)road|murram|grade')
expWater = expectedOutput.str.contains('(?i)water')
expLearning = expectedOutput.str.contains('(?i)environment|learn')
df['expected_output'] = np.where(expClassrooms, 'Improved Learning Facilities/Classrooms',
                                 np.where(expRoad, 'Improved Roads',
                                          np.where(expWater, 'Improved Water Access',
                                                   np.where(expLearning, 'Improved Learning Environment', df['expected_output']))))

sectors = df['sector']
sectors.str.lower()
df['sector'] = sectors.str.capitalize()
print(df.describe())

import random
def linegraphfunction(dataplot, title, xlabel, ylabel, num):
    r = lambda: random.randint(0, 255)
    setStyles = ['-.', '--', '-', ':', 'o', '+']

    fig, ax = plt.subplots()
    # plt.figure()
    for i in range(0, num):
        ax.plot(years, dataplot.iloc[i], setStyles[i % 6], color='#%02X%02X%02X' % (r(), r(), r()),
                 label=dataplot.index[i])

    ax.legend(loc="upper left")
    ax.grid(which='both')
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.yaxis.set_major_formatter(FuncFormatter(y_fmt))

    plt.show()

def pandaPlot(subPlotObject, stacked, title, tilt):
    fig, axs = plt.subplots()
    subPlotObject.plot.bar(stacked=stacked, ax=axs)
    axs.yaxis.set_major_formatter(FuncFormatter(y_fmt))
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xticks(rotation=tilt)
    plt.grid(which='both')

def y_fmt(y, pos):
    decades = [1e9, 1e6, 1e3, 1e0]
    suffix = ["B", "M", "T", ""]
    if y == 0:
        return str(0)
    for i, d in enumerate(decades):
        if np.abs(y) >=d:
            val = y/float(d)
            signf = len(str(val).split(".")[1])
            if signf == 0:
                return '{val:d} {suffix}'.format(val=int(val), suffix=suffix[i])
            else:
                if signf == 1:
                    if str(val).split(".")[1] == "0":
                       return '{val:d} {suffix}'.format(val=int(round(val)), suffix=suffix[i])
                tx = "{"+"val:.{signf}f".format(signf = signf) +"} {suffix}"
                return tx.format(val=val, suffix=suffix[i])

                #return y
    return y

# 1 Grouped by County (Top 5, Lowest 5)
years = ['f2003_2004', 'f2004_2005', 'f2005_2006', 'f2006_2007', 'f2007_2008', 'f2008_2009', 'f2009_2010']
countyPlot = df.groupby(['county']).sum().sort_values('total_amount', ascending=False)[years]
linegraphfunction(countyPlot, "Yearly Costs for Top 10 Counties", "Years", "Total Funds", 10)

# 2 Grouped by Sector
sectorPlot = df.groupby(['sector']).sum().sort_values('total_amount', ascending=False)[years]
linegraphfunction(sectorPlot, "Yearly Costs for Top 10 Sectors", "Years", "Total Funds", 10)

# 3 Group by Completion per Sector
pandaPlot(df.groupby(['sector', 'implementation_status']).sum().total_amount.unstack().sort_values('Complete', ascending=False).head(8), True, 'Top 8 Sectors Expenditure by Implementation Status', 45)

# 4 Group by Completion per County
pandaPlot(df.groupby(['county', 'implementation_status']).sum().total_amount.unstack().sort_values('Complete', ascending=False).head(15), True, 'Top 15 County Expenditure by Implementation Status', 45)

# 5 No of Projects per County
pandaPlot(df.groupby('county')['objectid'].count().sort_values(ascending=False), False, 'No. of Projects Per County', 90)

# 6 No of Projects per Sector
pandaPlot(df.groupby('sector')['objectid'].count().sort_values(ascending=False), False, 'No. of Projects Per Sector', 45)

# 7 Estimated Output/ Actual Totals per Sector
pandaPlot(df.groupby('sector')['estimated_cost', 'total_amount'].sum().sort_values('estimated_cost', ascending=False).head(5), False, 'Estimates Output vs Actual Totals per Sector', 45)

# 8 Estimated Output/ Actual Totals per County
pandaPlot(df.groupby('county')['estimated_cost', 'total_amount'].sum().sort_values('total_amount', ascending=False), False, 'Estimates Output vs Actual Totals per County', 90)

# Import library for 3D plotting
from mpl_toolkits import mplot3d
import matplotlib.cm as cmp

Z = df.total_amount
X = df[['x', 'y']]
# X, Y = np.meshgrid(X.x, X.y)
plt.figure('Location Vs Total Amount', figsize=(7, 5))
ax = plt.axes(projection='3d')
# ax.scatter(X.x, X.y, Z)
# ax.plot_surface(X.x, X.y, z, rstride=1, cstride=1, cmap=cmp.coolwarm, linewidth=0, antialiased=False)

