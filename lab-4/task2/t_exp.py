import numpy
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

z = [data_male[i] - data_female[i] for i in range(min(len(data_male), len(data_female)))]
z_expect = expectation(z)
s_z = numpy.sqrt(variance(z, z_expect))
t = z_expect / (s_z / numpy.sqrt(len(z)))
print(t)
print(len(z))