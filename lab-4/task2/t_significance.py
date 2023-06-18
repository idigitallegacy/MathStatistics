from matplotlib import pyplot
from scipy.stats import t

data = []
f = []
t_exp = 1.479
df = 661
iter = [i/1000 for i in range(1000)]
for i in iter:
    data.append(t.ppf(i, df=df))
    f.append(t_exp)

pyplot.plot(iter, data, label="Student distribution")
pyplot.plot(iter, f, label="t-value experimental = " + str(t_exp))
pyplot.axvline(x=t.cdf(t_exp, df=df), color="purple", label="Maximal trust level = " + str(round(t.cdf(t_exp, df=df), 4)))
pyplot.suptitle("Student criteria")
pyplot.title("df = " + str(df), color="red")
pyplot.xlabel("Trust level (1 - alpha)")
pyplot.ylabel("t-value")
pyplot.legend()
pyplot.show()