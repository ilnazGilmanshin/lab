import pandas as pd
all_cars = pd.read_csv('./auto4.csv', 
                       delimiter=',', 
                       decimal='.', 
                       index_col = 'name')
all_cars = all_cars.drop(['origin', 'mpg', 'displ', 'yr', 'origin'], axis = 1)
print(all_cars)