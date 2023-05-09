import pandas
import numpy

data = pandas.read_csv("../../data/sex_bmi_smokers.csv", delimiter=",")
data_male = list(data.loc[(data['sex'] == 'male')]['bmi'])
data_female = list(data.loc[(data['sex'] == 'female')]['bmi'])
print("n_1 =", len(data_male))
print("n_2 =", len(data_female))
print("mu_1 =", numpy.mean(data_male))
print("mu_2 =", numpy.mean(data_female))
print("sigma_1^2 =", numpy.var(data_male))
print("sigma_2^2 =", numpy.var(data_female))
print("S^2 =", ((len(data_male) - 1) * numpy.var(data_male) + (len(data_female) - 1) * numpy.var(data_female)) / (len(data_male) + len(data_female) - 2))