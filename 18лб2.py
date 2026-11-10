import numpy as np
import matplotlib
import matplotlib.pyplot as plt
scores = np.genfromtxt('X_reduced_428.csv', delimiter=';')
loadings = np.genfromtxt('X_loadings_428.csv', delimiter=';')
values = np.dot(scores, loadings.T)
plt.imshow(values, cmap='Greys_r')
plt.axis('off')
plt.show()
print("Номер верного «логотипа мероприятия»: 6")