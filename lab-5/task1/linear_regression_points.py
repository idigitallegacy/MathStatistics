# Scatter for all independent data from price value

import pandas
import numpy
import matplotlib.pyplot as plt
import matplotlib

def normalize(data): # min-max
    n_data = list()
    for i in data:
        n_data.append((i - data.min()) / (data.max() - data.min()))
    return numpy.array(n_data)


data = pandas.read_csv("../../data/cars93.csv", delimiter=",")
cfc = normalize(data["MPG.city"])
hfc = normalize(data["MPG.highway"])
hp = normalize(data["Horsepower"])
price = normalize(data["Price"])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = numpy.outer(cfc.T, cfc)
Y = numpy.outer(hfc.T, hfc)
Z = numpy.outer(hp.T, hp)
C = 0.432 - 0.022 * cfc - 0.098 * hfc + 0.59 * hp

minn, maxx = C.min(), C.max()
norm = matplotlib.colors.Normalize(minn, maxx)
m = plt.cm.ScalarMappable(norm=norm, cmap='jet')
m.set_array([])
fcolors = m.to_rgba(C)

plt.suptitle("4D Scatter for predicted data (normalized to [0; 1])")

scatter1 = ax.scatter(cfc, hfc, hp, c=price, label="Real values")
scatter2 = ax.scatter(cfc, hfc, hp, c=C, marker='x', label="Predicted values")
colorbar1 = fig.colorbar(scatter1, shrink=0.5, aspect=10)
ax.set_xlabel('City MPG, vol./len.')
ax.set_ylabel('Highway MPG, vol./len.')
ax.set_zlabel('Power, hp')
colorbar1.set_label("Price, $ cond.")

plt.legend()
ax.view_init(15, 85)
plt.show()