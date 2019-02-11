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
ongoing = implementation.str.contains('(?i)ongoing|on going|on-going|incomplete|on - going|going|in progress|50%')
notStarted = implementation.str.contains('(?i)not started|not yet started|new|stalled|to start|not yet|yet to begin|ye to commence')
fundsReallocated = implementation.str.contains('(?i)allocated|allocation|rea located')
complete = implementation.str.contains('(?i)complete|done|purchased|roofed|coomplete|pipes laid|in use|rehebilitated|100%|repaired|coimplte|dug')
df['implementation_status'] = np.where(complete, 'Complete',
                                       np.where(ongoing, 'Ongoing',
                                                np.where(notStarted, 'Not Started',
                                                         np.where(fundsReallocated, 'Funds Re-allocated', df['implementation_status']))))

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

def lineGraphs():
    # Grouped by County (Top 5, Lowest 5)
    years = ['f2003_2004', 'f2004_2005', 'f2005_2006', 'f2006_2007', 'f2007_2008', 'f2008_2009', 'f2009_2010']
    countyPlot = df.groupby(['county']).sum()[years]

    # Grouped by Sector
    sectorPlot = df.groupby(['sector']).sum().sort_values('total_amount')[years]
    rowNos = len(sectorPlot)

    import random
    r = lambda: random.randint(0, 255)
    color = '#%02X%02X%02X' % (r(), r(), r())

    setStyles = ['-.', '--', '-', ':', 'o', '+']

    for i in range(rowNos-10, rowNos):
        plt.plot(years, countyPlot.iloc[i], setStyles[i%6], color='#%02X%02X%02X' % (r(), r(), r()), label=countyPlot.index[i])

    plt.legend(loc="upper left")

    plt.title("Yearly Costs Per County", fontsize=16, fontweight='bold')
    plt.xlabel("Years")
    plt.ylabel("Total Funds")

    plt.show()

    plt.figure()
    for i in range(0, 15):
        plt.plot(years, sectorPlot.iloc[i], setStyles[i%6], color='#%02X%02X%02X' % (r(), r(), r()), label=sectorPlot.index[i])

    plt.legend(loc="upper left")

    plt.title("Yearly Costs Per Sector", fontsize=16, fontweight='bold')
    plt.xlabel("Years")
    plt.ylabel("Total Funds")

    plt.show()

# lineGraphs()

# Group by Completion per Sector
completionSector = df.groupby(['sector', 'implementation_status']).sum().sort_values('sector', ascending=True)['total_amount']
print(completionSector)

# Group by Total Amount/ Estimated Amount per Sector