from matplotlib import pyplot
from scipy.stats import t

data = []
f = []
n = 676
m = 662
t_exp = 1.71

df = n + m - 2

iter = [i/10000 for i in range(10000)]
for i in iter:
    data.append(t.ppf(1 - i, df=df))
    f.append(t_exp)

pyplot.plot(iter, data, label="t' distribution")
pyplot.plot(iter, f, label="t value = " + str(t_exp))
pyplot.axvline(x=1 - t.cdf(1.71, df=df), color="purple", label="Maximal trust level = " + str(round(1 - t.cdf(1.71, df=df), 4)))
pyplot.suptitle("t' criteria")
pyplot.title("df = " + str(df), color="red")
pyplot.xlabel("Trust level (1 - alpha)")
pyplot.ylabel("t' value")
pyplot.legend()
pyplot.show()