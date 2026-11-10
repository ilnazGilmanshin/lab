import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

DATA = pd.read_csv('./candy-data11-2.csv', delimiter=',', index_col='competitorname')
train_data = DATA.drop(['Smarties candy', 'Skittles wildberry'])

X = pd.DataFrame(train_data.drop(['winpercent', 'Y'], axis=1))
y = pd.DataFrame(train_data['winpercent'])

reg = LinearRegression().fit(X, y)

skittles = DATA.loc['Skittles wildberry',:].to_frame().T
smarties = DATA.loc['Smarties candy',:].to_frame().T

skittles_pred = reg.predict(skittles.drop(['winpercent', 'Y'], axis=1))
smarties_pred = reg.predict(smarties.drop(['winpercent', 'Y'], axis=1))

print("Предсказанное значение winpercent для конфеты Skittles wildberry:", skittles_pred)
print("Предсказанное значение winpercent для конфеты Smarties candy:", smarties_pred)