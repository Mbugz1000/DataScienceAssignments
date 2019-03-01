import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from sklearn.cluster import KMeans

miniProjectLoc = "C:\\Users\\ktmbugua\\Documents\\Digital Academy\\Data  Science\\MiniProject\\"
def cleaning_dataset(dataframe):
    dataframe.drop(columns=['index_', 'remarks', 'prox2', 'district', 'constituency', 'location', 'total_amount'], inplace=True)
    dataframe['total_amount'] = dataframe[['f2003_2004', 'f2005_2006', 'f2004_2005',  'f2006_2007', 'f2007_2008', 'f2008_2009', 'f2009_2010']].sum(axis=1)
    activities = dataframe['activity_to_bedone']
    classroom = activities.str.contains('(?i)classroom')
    latrines = activities.str.contains('(?i)latrines|toilet')
    classroomLatrines = (classroom & latrines)
    roadRepair = activities.str.contains('(?i)murram|road|grading')
    dispensary = activities.str.contains('(?i)dispensary')
    dataframe['activity_to_bedone'] = np.where(roadRepair, 'Road Repair',
                                               np.where(classroom, 'Construction/Renovation of Classrooms',
                                                        np.where(latrines, 'Construction of Latrines',
                                                                 np.where(classroomLatrines, 'Construction/Renovation of Classrooms and Latrines',
                                                                          np.where(dispensary, 'Construction of Dispensary', dataframe['activity_to_bedone'])))))

    implementation = dataframe['implementation_status']
    ongoing = implementation.str.contains('(?i)ongoing|on going|on-going|incomplete|on - going|going|in progress|50%|tendering|pending|ongoi|gpomg|still requires|plastering|painting|started')
    notStarted = implementation.str.contains('(?i)not started|not yet started|new|stalled|to start|not yet|yet to begin|ye to commence|not stated|to comenc|to commence|to be started')
    fundsReallocated = implementation.str.contains('(?i)allocated|allocation|rea located|realloca')
    complete = implementation.str.contains('(?i)complete|done|purchased|roofed|coomplete|pipes laid|in use|rehebilitated|100%|repaired|coimplte|dug|rehabilitated|bed made|plastered|renovated|in place')
    dataframe['implementation_status'] = np.where(complete, 'Complete',
                                                  np.where(ongoing, 'Ongoing',
                                                    np.where(notStarted, 'Not Started',
                                                             np.where(fundsReallocated, 'Funds Re-allocated', 'Other'))))

    expectedOutput = dataframe['expected_output']
    expClassrooms = expectedOutput.str.contains('(?i)class|facilities|edu|education')
    expRoad = expectedOutput.str.contains('(?i)road|murram|grade')
    expWater = expectedOutput.str.contains('(?i)water')
    expLearning = expectedOutput.str.contains('(?i)environment|learn')
    dataframe['expected_output'] = np.where(expClassrooms, 'Improved Learning Facilities/Classrooms',
                                            np.where(expRoad, 'Improved Roads',
                                                     np.where(expWater, 'Improved Water Access',
                                                              np.where(expLearning, 'Improved Learning Environment', dataframe['expected_output']))))

    sectors = dataframe['sector']
    sectors.str.lower()
    dataframe['sector'] = sectors.str.capitalize()
    dataframe = dataframe[dataframe.total_amount != 1]
    dataframe = dataframe[dataframe.total_amount != 2]

    # Remove projects that received nothing
    return dataframe[dataframe.total_amount != 0]

df = cleaning_dataset(pd.read_csv(miniProjectLoc + "CDF_Expenditure_on_Projects.csv"))
describe = df.describe()
df.info()

def pandalineplot(subPlotObject, title="", tilt=0, yearsbool=True, transptablebool=True):
    years = ['f2003_2004', 'f2004_2005', 'f2005_2006', 'f2006_2007', 'f2007_2008', 'f2008_2009', 'f2009_2010']
    fig, axs = plt.subplots()
    if yearsbool:
        subPlotObject = subPlotObject[years]

    if transptablebool:
        subPlotObject = subPlotObject.stack().unstack(level=0)

    subPlotObject.plot(ax=axs)
    axs.yaxis.set_major_formatter(FuncFormatter(y_fmt))
    axs.set_xticks(range(len(years)))
    axs.set_xticklabels(years)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xticks(rotation=tilt)
    plt.grid(which='both')

def pandabarplot(subPlotObject, stacked=True, title="", tilt=90, yearsbool=False,):
    years = ['f2003_2004', 'f2004_2005', 'f2005_2006', 'f2006_2007', 'f2007_2008', 'f2008_2009', 'f2009_2010']
    fig, axs = plt.subplots()
    if yearsbool:
        subPlotObject = subPlotObject[years]
    subPlotObject.plot.bar(stacked=stacked, ax=axs)
    axs.yaxis.set_major_formatter(FuncFormatter(y_fmt))
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xticks(rotation=tilt)
    plt.grid(which='both')

def knnml(columns, title):
    x = df[columns].fillna(0)

    kmeans = KMeans(n_clusters=3, random_state=0)
    y_kmeans = kmeans.fit_predict(x)

    # Visualising the clusters
    fig, axs = plt.subplots()
    axs.scatter(x.iloc[y_kmeans == 0, 0], x.iloc[y_kmeans == 0, 1], s=10, c='red', label='Low Exp Projects')
    axs.scatter(x.iloc[y_kmeans == 1, 0], x.iloc[y_kmeans == 1, 1], s=10, c='blue', label='High Exp Projects')
    axs.scatter(x.iloc[y_kmeans == 2, 0], x.iloc[y_kmeans == 2, 1], s=10, c='cyan', label='Medium Exp Projects')
    axs.yaxis.set_major_formatter(FuncFormatter(y_fmt))
    plt.title(title, fontsize=16, fontweight='bold')

    # Plotting the centroids of the clusters
    axs.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=25, c='yellow', label='Centroids')
    plt.grid(which='both')
    plt.legend()

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

def allgraphs():
    # 1 Grouped by County (Top 5, Lowest 5)
    pandalineplot(df.groupby(['county']).sum().sort_values('total_amount', ascending=False).head(10),
                  "Yearly Costs for Top 10 Counties")

    # 2 Group by Completion per County
    pandabarplot(df.groupby(['county', 'implementation_status']).sum().total_amount.unstack().sort_values
              ('Ongoing', ascending=False).head(15), title='Top 15 Counties by Expenditure and Implementations Status', tilt=45)


    # 3 No. of Projects funded per year
    pandabarplot(df.astype(bool).sum(), False, "Total no. of Projects Funded Per Year", 0, True)

    # 4,5 Expenditure clusters at various years
    knnml(['x', 'y', 'f2007_2008', 'f2006_2007'], 'Expenditure Clusters between 2006-2008')
    knnml(['x', 'y', 'f2004_2005', 'f2003_2004'], 'Expenditure Clusters between 2003-2005')

allgraphs()

