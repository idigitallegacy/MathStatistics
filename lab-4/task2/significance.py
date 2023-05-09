from matplotlib import pyplot
from scipy.stats import chi2

data = []
f = []
chi_exp = 28.76
df = 33.0
iter = [i/1000 for i in range(1000)]
for i in iter:
    data.append(chi2.ppf(i, df=df))
    f.append(chi_exp)

pyplot.plot(iter, data, label="Chi-squared distribution")
pyplot.plot(iter, f, label="Chi-squared value = " + str(chi_exp))
pyplot.axvline(x=chi2.cdf(chi_exp, df=df), color="purple", label="Maximal trust level = " + str(round(chi2.cdf(chi_exp, df=df), 4)))
pyplot.suptitle("Chi-squared criteria")
pyplot.title("df = " + str(df), color="red")
pyplot.xlabel("Trust level (1 - alpha)")
pyplot.ylabel("Chi-squared value")
pyplot.legend()
pyplot.show()