import pandas
import math
import numpy
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


def find_imperic_function(maxv, dataframe, step_x=0.01):
    y = 0
    sum = 0
    xval = []
    yval = []
    while y < maxv:
        for x in dataframe:
            if x < y:
                sum += 1
        sum /= len(dataframe)
        xval.append(y)
        yval.append(sum)
        y += step_x

    return xval, yval


data = pandas.read_csv("../../data/sex_bmi_smokers.csv", delimiter=",")['bmi']
mu = expectation(data)
sigma = math.sqrt(variance(data, mu))

data_normalized = [(i - mu) / sigma for i in data]
xval, yval = find_imperic_function(max(data_normalized), data_normalized)

diff = [yval[i] - norm.cdf(x=xval[i]) for i in range(len(xval))]
abs_diff = numpy.abs(diff)
print(max(abs_diff))
print(len(data))