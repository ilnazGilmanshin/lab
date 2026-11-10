import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

DATA = pd.read_csv("kmeans17.csv", delimiter=',', index_col='Object')

coords = DATA.drop('Cluster', axis=1)

centroid = np.array([[5.5, 11.5], [10.57, 7.57], [7.5, 15.0]])

kmeans = KMeans(n_clusters=3, init=centroid, max_iter=100, n_init=1, random_state=42)
kmeans.fit(coords)
labels = kmeans.labels_

result_table = coords.copy()
result_table['Cluster'] = labels
print("Результаты кластеризации")
print(result_table)

centroid_0 = kmeans.cluster_centers_[0]
cluster_0_objects = coords[labels == 0]

distances = np.sqrt(
    (cluster_0_objects['X'] - centroid_0[0])**2 + 
    (cluster_0_objects['Y'] - centroid_0[1])**2
)
mean_distance = distances.mean()
print(f"Среднее расстояние до центроида 0: {mean_distance:.3f}")