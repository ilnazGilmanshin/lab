import pandas as pd
data = pd.read_csv('./SPFB51.csv', 
                       delimiter=',', 
                       decimal='.')
data['DATE'] = data['<DATE>'] + ' ' + data['<TIME>'] 
data['DATE'] = pd.to_datetime(data['DATE'], format="%d/%m/%y %H:%M")
df_filtered = data[data['DATE'].dt.strftime('%Y-%m-%d') == '2018-09-06']
df_filtered = df_filtered.set_index('DATE')
df_filtered = df_filtered[['<OPEN>','<HIGH>','<LOW>','<CLOSE>']]
df_filtered.columns =['open', 'high', 'low', 'close']
d2 = df_filtered.resample('1h').agg({'open':'first',
                                     'high':'max',
                                     'low':'min',
                                     'close':'last'})
import plotly.graph_objects as go

fig = go.Figure(data=[go.Candlestick(x=d2.index,
                open=d2['open'],
                high=d2['high'],
                low=d2['low'],
                close=d2['close'])])

fig.show()

#print(df_filtered)