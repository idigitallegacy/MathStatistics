from matplotlib import pyplot
from scipy.stats import t

data = []
f = []
n = 274
m = 1064
t_exp = 0.12
S_x_sqr = 39.78
S_y_sqr = 36.48

df_x = n - 1
df_y = m - 1
nu_x = S_x_sqr / n
nu_y = S_y_sqr / m

iter = [i/10000 for i in range(10000)]
for i in iter:
    data.append((nu_x * t.ppf(1 - i, df=df_x) + nu_y * t.ppf(1 - i, df=df_y)) / (nu_x + nu_y))
    f.append(t_exp)

pyplot.plot(iter, data, label="t' distribution")
pyplot.plot(iter, f, label="t value = " + str(t_exp))
pyplot.axvline(x=0.45625, color="purple", label="Maximal trust level ~= 0.45625")
pyplot.suptitle("t' criteria")
pyplot.title("df_x = " + str(df_x) + "; " + "df_y = " + str(df_y), color="red")
pyplot.xlabel("Trust level (1 - alpha)")
pyplot.ylabel("t' value")
pyplot.legend()
pyplot.show()