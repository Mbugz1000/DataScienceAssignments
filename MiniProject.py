import pandas as pd
import numpy as np
# import pandas_profiling as pp
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\ktmbugua\\Documents\\Digital Academy\\Data  Science\\CDF_Expenditure_on_Projects.csv")
df.drop(columns=['index_', 'remarks', 'prox2', 'y', 'x', 'district', 'constituency', 'location'], inplace=True)
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

# def main():
#     report = pp.ProfileReport(df)
#     report.to_file(outputfile="C:\\Users\\ktmbugua\\Documents\\Digital Academy\\Data  Science\\MiniProjectProfile.html")
#
# if __name__ == "__main__" : main()

import random

def linegraphfunction(dataplot, title, xlabel, ylabel, num):
    r = lambda: random.randint(0, 255)
    setStyles = ['-.', '--', '-', ':', 'o', '+']

    plt.figure()
    for i in range(0, num):
        plt.plot(years, dataplot.iloc[i], setStyles[i % 6], color='#%02X%02X%02X' % (r(), r(), r()),
                 label=dataplot.index[i])

    plt.legend(loc="upper left")

    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()

# Grouped by County (Top 5, Lowest 5)
years = ['f2003_2004', 'f2004_2005', 'f2005_2006', 'f2006_2007', 'f2007_2008', 'f2008_2009', 'f2009_2010']
countyPlot = df.groupby(['county']).sum().sort_values('total_amount', ascending=False)[years]

linegraphfunction(countyPlot, "Yearly Costs Per County", "Years", "Total Funds", 8)

# Grouped by Sector
sectorPlot = df.groupby(['sector']).sum().sort_values('total_amount', ascending=False)[years]

linegraphfunction(sectorPlot, "Yearly Costs Per Sector", "Years", "Total Funds", 8)


def barchartfunction(mainDataFrame, groups, subgroups, num, xaxis):
    r = lambda: random.randint(0, 255)
    color = '#%02X%02X%02X' % (r(), r(), r())

    outerList = []
    for key2 in subgroups:
        bars = []
        for key1 in groups:
            try:
                bars.append(mainDataFrame[key1][key2])
            except KeyError:
                bars.append(0)
                continue

        outerList.append(bars)

    barWidth = 0.15

    # len(outerList[0])
    r1 = np.arange(num)
    plt.figure()
    for i, bars in enumerate(outerList):
        plt.bar(r1, bars[0:num], color='#%02X%02X%02X' % (r(), r(), r()), width=barWidth, edgecolor='white',label=subgroups[i])
        r1 = [x + barWidth for x in r1]

    # Add xticks on the middle of the group bars
    plt.xlabel(xaxis, fontweight='bold')
    plt.xticks([r2 + barWidth for r2 in range(num)], groups)

    # Create legend & Show graphic
    plt.legend()
    plt.show()

# Group by Completion per Sector
groups = df['sector'].unique()
subgroups = df['implementation_status'].unique()
completionSector = df.groupby(['sector', 'implementation_status']).sum().sort_values('total_amount', ascending=False)['total_amount']

barchartfunction(completionSector, groups, subgroups, 8, 'Sectors')

# Group by Total Amount/ Estimated Amount per Sector
countyGroups = df['county'].unique()
countySector = df.groupby(['county', 'implementation_status']).sum().sort_values('total_amount', ascending=False)['total_amount']

barchartfunction(countySector, countyGroups, subgroups, 8, 'Counties')

