import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from sklearn.cluster import KMeans
# Import library for 3D plotting
from mpl_toolkits import mplot3d
import matplotlib.cm as cmp
import random
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
df_cum = pd.read_csv(miniProjectLoc + "CDF_Cumulative_Expenditures_Constituencies.csv")
df_cum['total_amount'] = df_cum[['f2003_2004', 'f2005_2006', 'f2004_2005',  'f2006_2007', 'f2007_2008', 'f2008_2009', 'f2009_2010']].sum(axis=1)

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

def pandabarplot(subPlotObject, stacked=True, title="", tilt=90, yearsbool=False):
    years = ['f2003_2004', 'f2004_2005', 'f2005_2006', 'f2006_2007', 'f2007_2008', 'f2008_2009', 'f2009_2010']
    fig, axs = plt.subplots()
    if yearsbool:
        subPlotObject = subPlotObject[years]
    subPlotObject.plot.bar(stacked=stacked, ax=axs)
    axs.yaxis.set_major_formatter(FuncFormatter(y_fmt))
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xticks(rotation=tilt)
    plt.grid(which='both')

def scatterplot(dataframe, expenditure, title):
    Z = dataframe[expenditure]
    X = dataframe[['x', 'y']]
    plt.figure(title, figsize=(7, 5))
    ax = plt.axes(projection='3d')
    ax.scatter(X.x, X.y, Z)
    ax.zaxis.set_major_formatter(FuncFormatter(y_fmt))

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

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df_reg = df_cum.groupby(['county', 'population'])[['total_amount']].sum().reset_index()
X_train, X_test, y_train, y_test = train_test_split(df_reg[['population']], df_reg['total_amount'], random_state=0)
linreg = LinearRegression()
linreg.fit(X_train, y_train)

print('\nRegression Test set score: {:.2f}'.format(linreg.score(X_test, y_test)))
df_reg.plot.scatter(x='population', y='total_amount')
plt.plot(df_reg['population'], linreg.coef_*df_reg['population']+linreg.intercept_, 'r-')

def allgraphs():
    # 1 Grouped by County (Top 5, Lowest 5)
    pandalineplot(df.groupby(['county']).sum().sort_values('total_amount', ascending=False).head(10),
                  "Yearly Costs for Top 10 Counties")

    pandalineplot(df_cum.groupby(['county']).sum().sort_values('total_amount', ascending=False).head(10),
                  "Yearly Costs for Top 10 Counties DataSet 2")

    # 2 Grouped by Sector
    pandalineplot(df.groupby(['sector']).sum().sort_values('total_amount', ascending=False).head(10),
                  "Yearly Costs for Top 10 Sectors")

    # 3 Group by Completion per Sector
    pandabarplot(df.groupby(['sector', 'implementation_status']).sum().total_amount.unstack().sort_values
              ('Complete', ascending=False).head(8), title='Top 8 Sectors Expenditure by Implementation Status', tilt=45)

    # 4 Group by Completion per County
    pandabarplot(df.groupby(['county', 'implementation_status']).sum().total_amount.unstack().sort_values
              ('Ongoing', ascending=False).head(15), title='Top 15 County Expenditure by Implementation Status', tilt=45)

    # 5 No of Projects per County
    pandabarplot(df.groupby('county')['objectid'].count().sort_values(ascending=False), False, 'No. of Projects Per County')

    # 6 No of Projects per Sector
    df_per_sector = df.groupby('sector')['objectid'].count().sort_values(ascending=False)
    pandabarplot(df_per_sector, False, 'No. of Projects Per Sector', 45)

    def pietest():
        fig1, ax1 = plt.subplots()
        df_per_sector.plot.pie(ax=ax1, autopct='%1.1f%%', legend=True)  # autopct is show the % on plot
        ax1.axis('equal')
        plt.show()

    # 7 Estimated Output/ Actual Totals per Sector
    pandabarplot(df.groupby('sector')['estimated_cost', 'total_amount'].sum().sort_values('estimated_cost', ascending=False)
                 .head(8), False, 'Estimates Output vs Actual Totals for Top 8 Sectors', 45)

    # 8 Estimated Output/ Actual Totals per County
    pandabarplot(df.groupby('county')['estimated_cost', 'total_amount'].sum().sort_values('estimated_cost', ascending=False)
                 .head(25), False, 'Estimates Output vs Actual Totals for Top 15 Counties', 45)

    # 9 No. of Projects funded per year
    pandabarplot(df.astype(bool).sum(), False, "No. of Projects Funded Per Year", 0, True)

# 10 Projects that received funding in 2006 - 2007
df_2007 = df[df.f2006_2007 != 0]
# df_2007.to_csv(miniProjectLoc + "CDF_2007.csv", sep=',', encoding='utf-8')
# scatterplot(df_2007, 'f2006_2007', 'Location Vs 2006-2007 Amount')

# 11 Ongoing Projects after the 7 years
df_ongoing = df[df.implementation_status == 'Ongoing']
# df_ongoing.to_csv(miniProjectLoc + "CDF_Ongoing.csv", sep=',', encoding='utf-8')
# scatterplot(df_ongoing, 'total_amount', 'Location Vs Total Amount')

# 12 Projects that received funding in 2005 - 2006
df_2007 = df[df.f2005_2006 != 0]
# df_2007.to_csv(miniProjectLoc + "CDF_2006.csv", sep=',', encoding='utf-8')
# print(np.exp(np.linspace(0.0, 21.0, 0.5)))
print(np.exp([x/10 for x in range(0, 18, 5)]))
x = range(1, 20)
print(x)

years = ['f2003_2004', 'f2005_2006', 'f2004_2005',  'f2006_2007', 'f2007_2008', 'f2008_2009', 'f2009_2010']
df['total_amount_categ'] = pd.cut(df.total_amount, labels=range(1, 20), bins=np.exp([x/10 for x in range(0, 200, 5)])).dropna()
df['total_amount_int'] = df.total_amount_categ.astype(int)
print(np.exp(np.linspace(0, 0.5, 21)))
plt.figure()
df_p = df.groupby('total_amount_categ')['total_amount'].count()
print(df_p)
df_p.plot.bar()

def knnml(columns):
    x = df[columns].fillna(0)

    kmeans = KMeans(n_clusters=3, random_state=0)
    y_kmeans = kmeans.fit_predict(x)

    # Visualising the clusters
    plt.figure()
    plt.scatter(x.iloc[y_kmeans == 0, 0], x.iloc[y_kmeans == 0, 1], s=10, c='red', label='Cluster 1')
    plt.scatter(x.iloc[y_kmeans == 1, 0], x.iloc[y_kmeans == 1, 1], s=10, c='blue', label='Cluster 2')
    plt.scatter(x.iloc[y_kmeans == 2, 0], x.iloc[y_kmeans == 2, 1], s=10, c='green', label='Cluster 3')

    # Plotting the centroids of the clusters
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=25, c='yellow', label='Centroids')
    plt.legend()
#
# knnml(['total_amount_int', 'f2007_2008', 'f2006_2007', 'x', 'y'])
# knnml(['x', 'y','total_amount_int', 'f2007_2008', 'f2006_2007'])