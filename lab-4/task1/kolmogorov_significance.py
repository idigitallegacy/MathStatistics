from matplotlib import pyplot
from scipy.stats import chi2
import numpy

inf = 1000
data = []
f = []
chi_exp = 68.14
df = 38.0

iter = [i/1000 for i in range(2000)]
for t in iter:
    summa = 0
    for i in range(0 - inf, inf):
        summa += pow(-1, i) / numpy.exp(2 * pow(i, 2) * pow(t, 2))
    data.append(summa)

pyplot.plot(iter, data, label="Kolmogorov distribution")
pyplot.axvline(x=0.852, color="orange", label="sqrt(n)*D_n")
pyplot.axhline(y=0.54, color="purple", label="Intersection (K(t) = 0.54)")
pyplot.suptitle("Kolmogorov criteria")
pyplot.xlabel("t")
pyplot.ylabel("Distribution value")
pyplot.legend()
pyplot.show()