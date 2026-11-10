import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('71_36_18.csv', header=None)
X = df.values

X_scaled = StandardScaler().fit_transform(X)

pca = PCA(n_components=10, svd_solver='full') 
X_transformed = pca.fit_transform(X_scaled)

coord_1 = X_transformed[0, 0]
print(f"1. Координата 1-го объекта по 1-й ГК: {round(coord_1, 3)}")
coord_2 = X_transformed[0, 1]
print(f"2. Координата 1-го объекта по 2-й ГК: {round(coord_2, 3)}")
variance_2 = np.sum(pca.explained_variance_ratio_[:2])
print(f"3. Доля дисперсии первых двух ГК: {round(variance_2, 3)}")

cum_var = np.cumsum(pca.explained_variance_ratio_)
n_components_85 = np.argmax(cum_var > 0.85) + 1
print(f"4. Мин. кол-во ГК для дисперсии > 0.85: {n_components_85}")

plt.figure(figsize=(8, 6))
plt.scatter(X_transformed[:, 0], X_transformed[:, 1], c='blue', edgecolor='k', s=50)
plt.title('Проекция на первые две главные компоненты')
plt.xlabel('ГК 1')
plt.ylabel('ГК 2')
plt.grid(True)
plt.show()

print("5. Количество групп объектов по графику: 6")