import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import matplotlib.pyplot as plt

data = pd.read_csv('./candy-data14.csv', index_col='competitorname')

exclude_candies = ['Chewey Lemonhead Fruit Mix', 'Runts', 'Sixlets']
train_data = data.drop(exclude_candies)

X_train = train_data.drop(columns=['Y', 'winpercent'])
y_train = train_data['Y']

reg = LogisticRegression(random_state=2019, solver='lbfgs')
reg.fit(X_train, y_train)

test_data = pd.read_csv('./candy-test14.csv', index_col='competitorname')

X_test = test_data.drop(columns=['Y', 'winpercent'], errors='ignore')
y_true = test_data['Y']

y_probs = reg.predict_proba(X_test)[:, 1]

print(f"1. Вероятность Sugar Babies: {y_probs[test_data.index.get_loc('Sugar Babies')]:.3f}")
print(f"2. Вероятность Whoppers: {y_probs[test_data.index.get_loc('Whoppers')]:.3f}")

y_pred = reg.predict(X_test)

# Матрица ошибок
tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_pred).ravel()

# Расчет метрик (Precision, Recall)
precision = tp / (tp + fp)
recall = tp / (tp + fn)

auc = metrics.roc_auc_score(y_true, y_probs)

print(f"3. Матрица ошибок (TN, FP, FN, TP): {tn, fp, fn, tp}")
print(f"4. Recall (TPR): {recall:.3f}")
print(f"5. Precision: {precision:.3f}")
print(f"6. AUC: {auc:.3f}")

fpr, tpr, _ = metrics.roc_curve(y_true, y_probs)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {auc:.3f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()