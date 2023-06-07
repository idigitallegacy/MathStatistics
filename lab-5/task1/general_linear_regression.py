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


X = numpy.column_stack((numpy.ones(len(hp)), cfc, hfc, hp))
y = price

coefficients = numpy.linalg.inv(X.T @ X) @ X.T @ y
lin_reg = X @ coefficients

print(coefficients)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y = numpy.meshgrid(cfc, hfc)
Z = numpy.outer(hp.T, hp)
C = numpy.outer(lin_reg.T, lin_reg).reshape(len(cfc), len(hfc))

minn, maxx = C.min(), C.max()
norm = matplotlib.colors.Normalize(minn, maxx)
m = plt.cm.ScalarMappable(norm=norm, cmap='jet')
m.set_array([])
fcolors = m.to_rgba(C)

plt.suptitle("4D Scatter for all data (normalized to [0; 1])")

scatter = ax.scatter(cfc, hfc, hp, c=price)
colorbar = fig.colorbar(scatter, shrink=0.5, aspect=10)
ax.set_xlabel('City MPG, vol./len.')
ax.set_ylabel('Highway MPG, vol./len.')
ax.set_zlabel('Power, hp')
colorbar.set_label("Price, $ cond.")


ax.view_init(15, 5)
plt.show()