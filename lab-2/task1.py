import copy
from numpy import ndarray, array as nparray, square as square_ndarray, subtract as diff_ndarray
from decimal import Decimal
from scipy.stats import laplace
import matplotlib.pyplot as plt


class LaplaceAnalyser:
    def __calculate_selection_alpha(self, selection: ndarray) -> Decimal:
        squared_alpha = Decimal(1/2) * Decimal(square_ndarray(selection).sum()) / Decimal(selection.size)
        return Decimal.sqrt(squared_alpha)

    def __calculate_mse_squared_diff(self, actual_selection: ndarray, predicted_selection: ndarray) -> ndarray:
        diff = diff_ndarray(actual_selection, predicted_selection)
        return square_ndarray(diff)

    def __estimate_alphas(self) -> None:
        for selection in self.__selections:
            selection['analysis']['estimated_alpha'] = self.__calculate_selection_alpha(selection['rvs'])

    def __calculate_thresholds(self) -> None:
        for selection in self.__selections:
            selection['analysis']['alpha_threshold'] = abs(selection['params']['scale'] - selection['analysis']['estimated_alpha'])

    def __calculate_dispersions(self) -> None:
        for selection in self.__selections:
            selection['analysis']['dispersion'] = selection['rvs'].var()

    def __calculate_mse(self) -> None:
        for selection in self.__selections:
            squared_threshold = self.__calculate_mse_squared_diff(selection['rvs'], selection['predicted_rvs'])
            mse = squared_threshold.sum() / squared_threshold.size
            selection['analysis']['mse'] = mse

    def generate_selections(self, n_selections: int, size: int) -> None:
        for i in range(n_selections):
            self.__selections.append({
                'rvs': laplace.rvs(loc=float(self.__beta), scale=float(self.__alpha), size=size),
                'params': {
                    'location': self.__beta,
                    'scale': self.__alpha,
                    'size': size
                },
                'analysis': {
                    # 'EstimatedAlpha': None,
                    # 'AlphaThreshold': None,
                    # 'Disperison': None,
                    # 'MeanSquaredError': None,
                },
            })

    def analyse(self) -> None:
        self.__estimate_alphas()
        for selection in self.__selections:
            selection['predicted_rvs'] = laplace.rvs(
                loc=float(selection['params']['location']),
                scale=float(selection['analysis']['estimated_alpha']),
                size=selection['params']['size']
            )
            selection['rvs'].sort()
            selection['predicted_rvs'].sort()
        self.__calculate_dispersions()
        self.__calculate_thresholds()
        self.__calculate_mse()

    def get(self) -> list:
        needle = [{"params": selection["params"], "analysis": selection["analysis"]} for selection in self.__selections]
        return needle

    def __init__(self, location: Decimal, scale: Decimal, threshold: Decimal):
        self.__alpha = scale
        self.__beta = location
        self.__threshold = threshold
        self.__selections = []


def plot_mse(collected_data):
    plot_data = {}
    for selection in collected_data:
        size = selection["params"]["size"]
        mse = selection["analysis"]["mse"]
        if size not in plot_data:
            plot_data[size] = [mse]
        else:
            plot_data[size].append(mse)
    plt.title("Mean Squared Error from selection size dependency", pad=10, fontsize=15)
    plt.xlabel("Selection size", fontsize=12)
    plt.ylabel("MSE", fontsize=12)
    plt.xlim([500, 2500])
    plt.ylim([0, 0.1])
    plt.plot(plot_data.keys(), plot_data.values())
    plt.savefig("./plots/laplace_mse.png")
    plt.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    alpha = Decimal('0.5')
    beta = Decimal('0.0')
    threshold = Decimal('0.01')
    n_selections = 500
    size_xs = 50
    size_s = 100
    size_m = 500
    size_l = 1000
    size_xl = 2500
    analyser = LaplaceAnalyser(location=beta, scale=alpha, threshold=threshold)

    analyser.generate_selections(n_selections, size_xs)
    analyser.generate_selections(n_selections, size_s)
    analyser.generate_selections(n_selections, size_m)
    analyser.generate_selections(n_selections, size_l)
    analyser.generate_selections(n_selections, size_xl)
    analyser.analyse()

    data = analyser.get()
    plot_mse(data)


    exit(0)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
