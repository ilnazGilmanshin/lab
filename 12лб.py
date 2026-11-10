import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

train_data = pd.read_csv('./Task_data12.csv', delimiter=',', index_col='id')

X = train_data[['X', 'Y']].values
y = train_data['Class'].values

new_object = [[74, 92]]

neigh_e = KNeighborsClassifier(n_neighbors=3, p=2)
neigh_e.fit(X, y)

dist_e, ind_e = neigh_e.kneighbors(new_object)

ids_e = ind_e[0] 

class_e = neigh_e.predict(new_object)[0]

print("ЕВКЛИДОВА МЕТРИКА")
print(f"Расстояние до ближайшего соседа: {dist_e[0][0]:.3f}")
print(f"ID трех ближайших точек: {','.join(map(str, ids_e))}")
print(f"Класс при k=3: {class_e}")

neigh_m = KNeighborsClassifier(n_neighbors=3, p=1)
neigh_m.fit(X, y)

dist_m, ind_m = neigh_m.kneighbors(new_object)
ids_m = ind_m[0]
class_m = neigh_m.predict(new_object)[0]

print("МАНХЭТТЕНСКАЯ МЕТРИКА")
print(f"Расстояние до ближайшего соседа: {dist_m[0][0]:.3f}")
print(f"ID трех ближайших точек: {','.join(map(str, ids_m))}")
print(f"Класс при k=3: {class_m}")