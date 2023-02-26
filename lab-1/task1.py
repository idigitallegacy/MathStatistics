from scipy.stats import bernoulli
from decimal import Decimal
import matplotlib.pyplot as plt

parameter = Decimal('2.0')/Decimal('3.0')  # 2/3 испытаний - успешны
epsilon = Decimal('0.01')  # отклонение выборочного среднего от мат. ожидания = p
size = 8537  # размер выборки (см. отчет)

x_array = [i for i in range(500)]
data = []
eps_data = [epsilon for i in range(500)]

n = 0  # Счтетчик количества отклонений
for i in range(500):
    selection = bernoulli.rvs(p=float(parameter), size=size)  # выборка
    selection_mean = Decimal(str(selection.sum())) / Decimal(str(size))  # выборочное среднее
    if abs(selection_mean - parameter) > epsilon:
        n += 1
    data.append(abs(selection_mean - parameter))

print(n)

plt.plot(x_array, data)
plt.plot(x_array, eps_data)
plt.xlabel("Sample")
plt.ylabel("Variation")
plt.show()
