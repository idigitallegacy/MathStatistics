# This file is only written to display distribution functions
import numpy
import scipy
from matplotlib import pyplot as plt

def distribution_function(low, high):
    x = [i / 100 for i in range(low, high)]
    x_inner = [(pow(i, 3) - 5) / numpy.sqrt(2) for i in x]
    f = numpy.multiply(1 / 2, scipy.special.erf(x_inner))
    f = numpy.add(1 / 2, f)
    return [x, f]


df = distribution_function(-100, 400)
plt.title("Distribution function with theta = 5, C = 1/2", pad=10, fontsize=15)
plt.xlabel("X", fontsize=12)
plt.ylabel("Probability", fontsize=12)
plt.plot(df[0], df[1])
plt.show()