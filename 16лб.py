from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import graphviz
import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('diabetes16.csv') 
df.head()
task_data = df.head(690)

print("1. Число строк класса 0:", len(task_data[task_data['Outcome'] == 0]))

train = task_data.head(int(len(task_data)*0.8))
test = task_data.tail(int(len(task_data)*0.2))

features = list(train.columns[:8])
x = train[features]
y = train['Outcome']

tree = DecisionTreeClassifier(criterion='entropy',      # критерий разделения
                              min_samples_leaf=10,      # минимальное число объектов в листе
                              max_leaf_nodes=20,        # максимальное число листьев
                              random_state=2020)
clf = tree.fit(x, y)

columns = list(x.columns)
export_graphviz(clf, out_file='tree.dot', 
                feature_names=columns,
                class_names=['0', '1'],
                rounded = True, proportion = False, 
                precision = 2, filled = True, label='all')

with open('tree.dot') as f:
    dot_graph = f.read()

graphviz.Source(dot_graph)

print("4. Глубина дерева:", clf.tree_.max_depth)

used_features = clf.tree_.feature[clf.tree_.feature >= 0]
used_thresholds = clf.tree_.threshold[clf.tree_.feature >= 0]

last_idx = used_features[-1]
last_threshold = used_thresholds[-1]

print("4. Предиктор на последнем уровне:", features[last_idx])
print("4. Значение разделения: {:.2f}".format(last_threshold))

x_test = test[features]
y_true = test['Outcome']
y_pred = clf.predict(x_test)

print("5. Доля правильных ответов: {:.2f}".format(accuracy_score(y_true, y_pred)))
print("5. Среднее значение метрик (Macro-F1): {:.2f}".format(f1_score(y_true, y_pred, average='macro')))

for pid in [727, 710, 704, 729]:
    patient_features = df.loc[[pid], features] 
    pred = clf.predict(patient_features)[0]
    print(f"6. Предсказание для пациента с {pid}: {pred}")