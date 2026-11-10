import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data_series = pd.read_csv('./task7.csv')
data_series.index += 1
def exponential_smoothing(series, alpha):
    result = [series[0]]
    for index in range(1, len(series)):
        result.append(alpha * series[index] + (1 - alpha) * result[index - 1]) 
    return result
data_series['y_exp_norm_user'] = exponential_smoothing(data_series['y'].to_list(), 0.2)

print(data_series)

v58 = data_series['y_exp_norm_user'].iloc[57]
print(f"58-я точка: {round(v58, 2)}")

v100 = data_series['y_exp_norm_user'].iloc[-1]
print(f"100-я точка: {round(v100, 2)}")

x = np.arange(1, 101)
y = data_series['y'].values
a, b = np.polyfit(x, y, 1)
print(f"a = {round(a, 2)}, b = {round(b, 2)}")

y_pred = a * x + b
ss_res = np.sum((y - y_pred) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r2 = 1 - ss_res / ss_tot
print(f"R² = {round(r2, 2)}")

forecast = a * 101 + b
print(f"Прогноз 101-й точки: {round(forecast)}")

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Исходный ряд', alpha=0.5)
plt.plot(x, data_series['y_exp_norm_user'], label='Сглаженный ряд', color='orange')
plt.plot(x, y_pred, label='Линейный тренд', color='red', linestyle='--')
plt.scatter([101], [forecast], color='green', zorder=5, label='Прогноз 101')
plt.legend()
plt.grid(True)
plt.show()