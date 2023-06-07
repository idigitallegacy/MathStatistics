import numpy
from scipy import stats
import pandas

def normalize(data): # min-max
    n_data = list()
    for i in data:
        n_data.append((i - data.min()) / (data.max() - data.min()))
    return numpy.array(n_data)

data = pandas.read_csv("../../data/cars93.csv", delimiter=",")
cfc = normalize(data["MPG.city"])
hfc = normalize(data["MPG.highway"])
price = normalize(data["Price"])

X = numpy.column_stack((numpy.ones(len(cfc)), cfc, hfc))
y = price
beta = numpy.linalg.inv(X.T @ X) @ X.T @ y

# Вычисляем остатки
y_hat = X.dot(beta)
residuals = price - y_hat

# Вычисляем стандартное отклонение остатков
residual_std = numpy.std(residuals, ddof=len(cfc) - X.shape[1])

# Вычисляем оценку ковариационной матрицы
X_transpose_X_inv = numpy.linalg.inv(X.T.dot(X))
cov_matrix = residual_std**2 * X_transpose_X_inv

# Вычисляем стандартные ошибки коэффициентов
se = numpy.sqrt(numpy.diag(cov_matrix))

# Вычисляем t-статистику и p-значение
t_statistic = beta / se
p_value = 2 * (1 - stats.t.cdf(numpy.abs(t_statistic), len(cfc) - X.shape[1]))

# Выводим результаты теста
for i, coef in enumerate(beta):
    print(f'Коэффициент beta_{i}:')
    print(f'Значение: {coef}')
    print(f't-статистика: {t_statistic[i]}')
    print(f'p-значение: {p_value[i]}\n')