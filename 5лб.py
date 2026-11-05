import pandas as pd
answers = pd.read_excel('./var5.xlsx')
to_plot = pd.DataFrame(answers['Choice_1'].value_counts())
to_plot.columns = ['Amount']
to_plot = to_plot.sort_index()
import matplotlib.pyplot as plt

full_to_plot = pd.DataFrame(pd.DataFrame(answers.values.reshape(-1))[0].value_counts())
full_to_plot.columns = ['Amount']
full_to_plot = full_to_plot.sort_index()
full_to_plot

plt.pie(full_to_plot['Amount'], labels = full_to_plot.index)
plt.show()