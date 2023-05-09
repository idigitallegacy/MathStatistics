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


data = pandas.read_csv("../../data/sex_bmi_smokers.csv", delimiter=",")
data_male = list(data.loc[(data['sex'] == 'male')]['bmi'])
data_female = list(data.loc[(data['sex'] == 'female')]['bmi'])

mu_male = expectation(data_male)
mu_female = expectation(data_female)
sigma_male = math.sqrt(variance(data_male, mu_male))
sigma_female = math.sqrt(variance(data_female, mu_female))

dk = 1
lower_bound = min(min(data_male), min(data_female))
upper_bound = max(max(data_male), max(data_female))
n_intervals = math.ceil((upper_bound - lower_bound) / dk)
step = (upper_bound - lower_bound) / n_intervals

data_male_amount = [0 for i in range(n_intervals)]
data_female_amount = [0 for i in range(n_intervals)]

for i in data_male:
    for j in range(n_intervals):
        if j * step + lower_bound <= i < j * step + step + lower_bound:
            data_male_amount[j] = data_male_amount[j] + 1
        elif j == n_intervals - 1 and j * step + step + lower_bound <= i:
            data_male_amount[j] = data_male_amount[j] + 1

for i in data_female:
    for j in range(n_intervals):
        if j * step + lower_bound <= i < j * step + step + lower_bound:
            data_female_amount[j] = data_female_amount[j] + 1
        elif j == n_intervals - 1 and j * step + step + lower_bound <= i:
            data_female_amount[j] = data_female_amount[j] + 1

data_male_expected = [(data_male_amount[i] + data_female_amount[i]) * sum(data_male_amount) / (sum(data_male_amount) + sum(data_female_amount)) for i in range(n_intervals)]
data_female_expected = [(data_male_amount[i] + data_female_amount[i]) * sum(data_female_amount) / (sum(data_male_amount) + sum(data_female_amount)) for i in range(n_intervals)]
flag = False
for i in range(n_intervals):
    if i == len(data_male_expected):
        break
    if not flag:
        if data_male_expected[i] != 0.0 and data_female_expected[i] != 0.0:
            data_male_amount = data_male_amount[i:]
            data_female_amount = data_female_amount[i:]
            data_male_expected = data_male_expected[i:]
            data_female_expected = data_female_expected[i:]
            flag = True
    if flag:
        if data_male_expected[i] == 0.0 and data_female_expected[i] == 0.0:
            data_male_amount = data_male_amount[:i]
            data_female_amount = data_female_amount[:i]
            data_male_expected = data_male_expected[:i]
            data_female_expected = data_female_expected[:i]
            break
n_intervals = len(data_male_expected)


chi_squared_male = [pow(data_male_amount[i] - data_male_expected[i], 2) / data_male_expected[i] for i in range(n_intervals)]
chi_squared_female = [pow(data_female_amount[i] - data_female_expected[i], 2) / data_female_expected[i] for i in range(n_intervals)]
print("Non-null intervals amount:", n_intervals)
print("Chi-squared value:", sum(chi_squared_male) + sum(chi_squared_female))