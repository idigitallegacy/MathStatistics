import pandas
import math
from scipy.stats import norm

def expectation(data):
    sum = 0
    for i in data:
        sum = sum + i
    return sum / len(data)


def variance(data, mu):
    sum = 0
    for i in data:
        sum = sum + pow(i - mu, 2)
    return sum / (len(data) - 1)


data = pandas.read_csv("../../data/sex_bmi_smokers.csv", delimiter=",")['bmi']
mu = expectation(data)
sigma = math.sqrt(variance(data, mu))
data_normalized = [(i - mu) / sigma for i in data]
data_min = min(data)
data_max = max(data)
data_normalized_min = min(data_normalized)
data_normalized_max = max(data_normalized)

P = []

dk = 1
n_intervals = math.ceil((data_max - data_min) / dk)
step = (data_normalized_max - data_normalized_min) / n_intervals
n_i = [0 for i in range(n_intervals)]

for i in data_normalized:
    for j in range(n_intervals):
        if j * step + data_normalized_min <= i < j * step + step + data_normalized_min:
            n_i[j] = n_i[j] + 1
        elif j == n_intervals - 1 and j * step + step + data_normalized_min <= i:
            n_i[j] = n_i[j] + 1

for i in range(n_intervals):
    P.append(norm.cdf(i * step + step + data_normalized_min) - norm.cdf(i * step + data_normalized_min))
P_sq = []
for i in range(n_intervals):
    P_sq.append(pow((n_i[i] / len(data_normalized)) - P[i], 2) / P[i])

print("Amount of intervals:", n_intervals)
print("Chi-squared value:", len(data_normalized) * sum(P_sq))