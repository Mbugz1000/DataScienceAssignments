import sys
print("Python version:", sys.version)

import pandas as pd
print("pandas version:", pd.__version__)

import matplotlib
print("matplotlib version:", matplotlib.__version__)

import numpy as np
print("NumPy version:", np.__version__)

import sklearn
print("scikit-learn version:", sklearn.__version__)

from sklearn.datasets import load_iris
iris_dataset = load_iris()

# Converting a Sklearn Bunch into a Pandas DataFrame
iris = pd.DataFrame(data=iris_dataset["data"], columns=iris_dataset["feature_names"])
iris["target"] = iris_dataset["target"]

# Training and Testing Data
from sklearn.model_selection import train_test_split
# X is taken as the independent variable and Y the dependent (the last row i.e. target)
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

# Building the model: k-Nearest Neighbours
from sklearn.neighbors import KNeighborsClassifier
# TODO Read on how this Classifier Works
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)

# Making Predictions
X_new = np.array([[5, 2.9, 1, 0.2]])

prediction = knn.predict(X_new)
print('\nPrediction:', prediction)
print('Predicted target name:', iris_dataset['target_names'][prediction])

# Evaluating the model
y_pred = knn.predict(X_test)  # Test set predictions
print("Test set predictions:\n", y_pred)

print('Test set score: (Using np.mean and knn.predict) {:.2f}'.format(np.mean(y_pred == y_test)))

print('Test set score: (Using knn.score) {:.2f}'.format(knn.score(X_test, y_test)))

# Building a regression Model
# TODO Read on how this Regression Model Works
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(iris[['petal length (cm)']], iris['petal width (cm)'], random_state=0)
linreg = LinearRegression()
linreg.fit(X_train, y_train)

print('\nRegression Test set score: {:.2f}'.format(linreg.score(X_test, y_test)))

# Plot regression line
import  matplotlib.pyplot as plt
# TODO Find out what the s=50 and alpha=0 do
plt.scatter(iris['petal length (cm)'], iris['petal width (cm)'], marker='o', s=50, alpha=0.8)
plt.plot(iris['petal length (cm)'], linreg.coef_*iris['petal length (cm)']+linreg.intercept_, 'r-')

plt.title('Petal Length (cm) vs Petal Width (cm)')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')


# Building a KMeans Model
from sklearn.cluster import KMeans
print(iris.columns)

x = iris[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']]
y = iris['target']
# TODO Read on how this model works
kmeans = KMeans(n_clusters=3, random_state=0)
y_kmeans = kmeans.fit_predict(x)

print('Accuracy set score: {:.2f}'.format(np.mean(y == y_kmeans)))

# Visualising the clusters
plt.figure()
plt.scatter(x.iloc[y_kmeans == 0, 0], x.iloc[y_kmeans == 0, 1], s=100, c='red', label='Iris-setosa')
plt.scatter(x.iloc[y_kmeans == 1, 0], x.iloc[y_kmeans == 1, 1], s=100, c='blue', label='Iris-versicolour')
plt.scatter(x.iloc[y_kmeans == 2, 0], x.iloc[y_kmeans == 2, 1], s=100, c='green', label='Iris-virginica')

# Plotting the centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='yellow', label='Centroids')

plt.legend()