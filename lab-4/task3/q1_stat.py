import pandas
import numpy

data = pandas.read_csv("../../data/sex_bmi_smokers.csv", delimiter=",")
data_smokers = list(data.loc[(data['smoker'] == 'yes')]['bmi'])
data_nonsmokers = list(data.loc[(data['smoker'] == 'no')]['bmi'])
print("n_1 =", len(data_smokers))
print("n_2 =", len(data_nonsmokers))
print("mu_1 =", numpy.mean(data_smokers))
print("mu_2 =", numpy.mean(data_nonsmokers))
print("sigma_1^2 =", numpy.var(data_smokers))
print("sigma_2^2 =", numpy.var(data_nonsmokers))
print("S^2 =", 1 / len(data_smokers) * numpy.var(data_smokers) + 1 / len(data_nonsmokers) * numpy.var(data_nonsmokers))