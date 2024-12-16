from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import numpy as np
import pandas as pd
import sklearn.metrics as metrics
import matplotlib.pyplot as plt

'''
class error idk

iris dataset - csv file
classes 
1. iris setosa
2. iris versicolor
3. iris virginica

x - features cols
y - labels - 0, 1, 2
'''

names = ['Sepal_length','Sepal_width','Petal_length','Petal_width','Class']
labels = {'Iris-Setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2}
dataset = pd.read_csv("8-dataset.csv",names=names)

x = dataset.iloc[:,:-1]
print(x)
print(dataset.iloc[:,-2])
y = [labels[c] for c in dataset.iloc[:,-1]]
print(y)
plt.figure(figsize=(14,7))
colormap = np.array(['red', 'lime', 'black'])

# REAL PLOT
plt.subplot(1,3,1)
plt.title('Real')
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y])

model = KMeans(n_clusters=3, random_state=3425).fit(x)

# KMeans
plt.subplot(1,3,2)
plt.title('KMeans')
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[model.labels_])

print('The accuracy score of K-Mean: ', metrics.accuracy_score(y, model.labels_))
print('The Confusion matrix of K-Mean:\n', metrics.confusion_matrix(y, model.labels_))

# Gaussian
gmm = GaussianMixture(n_components=3, random_state=3425).fit(x)
y_cluster_gmm = gmm.predict(x)

plt.subplot(1,3,3)
plt.title('GMM Classification')
plt.scatter(x.Petal_Length, x.Petal_Width, c=colormap[y_cluster_gmm])

print('The accuracy score of EM: ', metrics.accuracy_score(y, y_cluster_gmm))
print('The Confusion matrix of EM:\n', metrics.confusion_matrix(y, y_cluster_gmm))




