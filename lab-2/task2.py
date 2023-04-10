import math

import matplotlib.pyplot as plt
import numpy
import scipy


class Generator:
    def __match(self, sample, theta):
        value = numpy.multiply(numpy.sqrt(2), scipy.special.erfinv((1 / 2) * (2 * sample - 1)))
        value = numpy.add(theta, value)
        value = numpy.sign(value) * pow(numpy.abs(value), 1/3)
        return value

    def rvs(self, size, theta=5):
        initial_selection = numpy.random.uniform(0, 1, size)
        rvs = [self.__match(sample, theta) for sample in initial_selection]
        return rvs

def find_theta(selection):
    qubic_selection = numpy.power(selection, 3)
    selection_sum = numpy.sum(qubic_selection)
    return numpy.multiply(1/len(selection), selection_sum)

def find_mse(thetas, predicted_theta):
    diff = numpy.add(thetas, 0 - predicted_theta)
    square = numpy.power(diff, 2)
    summ = numpy.sum(square)
    return numpy.multiply(1/len(thetas), summ)


theta = 5
threshold = 0.01
sizes = [50, 100, 500, 1000, 2500, 5000]
generator = Generator()
for size in sizes:
    threshold_counter = 0
    thetas = []
    for i in range(500):
        rvs = generator.rvs(size)
        selection_theta = find_theta(rvs)
        thetas.append(selection_theta)
        if abs(theta - selection_theta) > threshold:
            threshold_counter += 1
    mse = find_mse(thetas, theta)
    print("Size: " + str(size) + ", threshold exceed: " + str(threshold_counter) + " of 500 times, MSE: " + str(mse) + ", RMSE: " + str(numpy.sqrt(mse)))