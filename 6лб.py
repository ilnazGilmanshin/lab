import pandas as pd
import numpy as np
data = pd.read_csv('./task6.csv',
                   delimiter=',',
                   decimal='.',
                   index_col='ID')
data = 1 - np.exp(1 - data / data.min())
data['SUM'] = data['DISTANCE'] + data['STOP_COUNT'] + data['COST']
data = data.sort_values(by='SUM', ascending=True)
top3 = data.head(3).index.tolist()
print(','.join(map(str, top3)))