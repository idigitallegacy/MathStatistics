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
price = normalize(data["Price"])

X = numpy.column_stack((numpy.ones(len(cfc)), cfc))
y = price

coefficients = numpy.linalg.inv(X.T @ X) @ X.T @ y
lin_reg = X @ coefficients

print(coefficients)
C = coefficients[0] + coefficients[1] * cfc

print(((y - C) ** 2).sum())
print((y ** 2).sum())

plt.suptitle("Regression for city MPG and price data (normalized to [0; 1])")

scatter = plt.scatter(cfc, price, label="Real values")
plt.plot(cfc, C, color="red", label="Predicted values")
plt.xlabel("City MPG, vol./len.")
plt.ylabel("Price, $ cond.")
plt.legend()
plt.show()