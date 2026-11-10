import pandas as pd
data = pd.read_csv('./indzad4.csv', 
                       delimiter=',', 
                       decimal='.')
sample_data = data[((data.TG == 0) & (data.MIP >= 96.921875) & (data.MIP <= 97.4140625)) | ((data.TG == 1) & (data.MIP >= 41.8828125) & (data.MIP <= 47.4140625))]
print(sample_data.MIP.mean())