import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as sch 
import matplotlib.pyplot as plt

# dataset
dataset = pd.read_csv('Mall_Customers.csv') 
X = dataset.iloc[:, [3, 4]].values

# dendrogram
dendrogram = sch.dendrogram(sch.linkage(X, method='ward')) 
plt.title('Dendrogram') 
plt.xlabel('Customers') 
plt.ylabel('Euclidean distances') 
plt.show()

# agglomertive clustering
from sklearn.cluster import AgglomerativeClustering 
hc = AgglomerativeClustering(n_clusters=5, metric='euclidean', linkage='ward') 
y_hc = hc.fit_predict(X)

colors = ['red', 'blue', 'green', 'cyan', 'magenta']
labels = [f'Cluster {i+1}' for i in range(5)]

for i, color, label in zip(range(5), colors, labels):
    plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], s=100, c=color, label=label)

plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
