import matplotlib.pyplot as plt
import pandas as pd

class BMICalculator:
    def __init__(self):
        self.__selection_mean = 0.0
        self.__selection_dispersion = 0.0
        self.__selection_median = 0.0
        self.__selection_quantile = 0.0
        self.__df = pd.DataFrame()

    def change_data_frame(self, dataframe: pd.DataFrame):
        self.__df = dataframe

    def calculate(self):
        self.__selection_mean = self.__df.mean()
        self.__selection_dispersion = pow(self.__df.std(), 2)  # Ст. отклонение ("сигма") в квадрате - есть дисперсия
        self.__selection_median = self.__df.median()
        self.__selection_quantile = self.__df.quantile(q=3 / 5)

    def print(self, heading):
        print(heading)
        print("\tMean value:", self.__selection_mean)
        print("\tDispersion:", self.__selection_dispersion)
        print("\tMedian value:", self.__selection_median)
        print("\tQuantile (q=3/5):", self.__selection_quantile)
        print()


class BMIPlotter:
    def __init__(self, dataframe: pd.DataFrame):
        self.__df = dataframe
        self.__selection_maxvalue = dataframe.max()
        self.__selection_minvalue = dataframe.min()
        self.__imperic_xvalues = []
        self.__imperic_yvalues = []

    def find_imperic_function(self, step_x=0.01):
        y = 0
        sum = 0
        while y < self.__selection_maxvalue:
            for x in self.__df:
                if x < y:
                    sum += 1
            sum /= len(self.__df)
            self.__imperic_xvalues.append(y)
            self.__imperic_yvalues.append(sum)
            y += step_x

    def plot_imperic(self):
        plt.plot(self.__imperic_xvalues, self.__imperic_yvalues)
        plt.xlabel('Value')
        plt.ylabel('Probability')
        plt.show()
        plt.close()

    def plot_histogram(self):
        plt.hist(self.__df, bins=30)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.show()
        plt.close()

    def plot_boxplot(self):
        plt.boxplot(self.__df)
        plt.show()
        plt.close()


data = pd.read_csv("sex_bmi_smokers.csv", delimiter=",")
male_smokers = data.loc[(data['sex'] == 'male') & (data['smoker'] == 'yes')]
female_smokers = data.loc[(data['sex'] == 'female') & (data['smoker'] == 'yes')]
female_healthy = data.loc[(data['sex'] == 'female') & (data['smoker'] == 'no')]
male_healthy = data.loc[(data['sex'] == 'male') & (data['smoker'] == 'no')]

print("Male smokers amount:", len(male_smokers))
print("Female smokers amount:", len(female_smokers))
print()

calculator = BMICalculator()
calculator.change_data_frame(data['bmi'])
calculator.calculate()
calculator.print("BMI overall")

calculator.change_data_frame(male_smokers['bmi'])
calculator.calculate()
calculator.print("BMI male smokers")

calculator.change_data_frame(male_healthy['bmi'])
calculator.calculate()
calculator.print("BMI male healthy")

calculator.change_data_frame(female_smokers['bmi'])
calculator.calculate()
calculator.print("BMI female smokers")

calculator.change_data_frame(female_healthy['bmi'])
calculator.calculate()
calculator.print("BMI female healthy")

plotter = BMIPlotter(data['bmi'])
plotter.find_imperic_function(1)
plotter.plot_imperic()
plotter.plot_histogram()
plotter.plot_boxplot()
