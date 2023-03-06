import copy
from numpy import ndarray, square as square_ndarray
from decimal import Decimal
from scipy.stats import laplace

class LaplaceAnalyser:
    def __int__(self, location: Decimal, scale: Decimal, threshold: Decimal):
        self.__alpha = scale
        self.__beta = location
        self.__threshold = threshold
        self.__selections = []

    def __calculate_selection_alpha(self, selection: ndarray) -> Decimal:
        squared_selection = square_ndarray(selection)
        return Decimal.sqrt(Decimal(2 * selection.size) / Decimal(squared_selection.sum()))

    def __estimate_alphas(self) -> None:
        for selection in self.__selections:
            selection['analysis']['estimated_alpha'] = self.__calculate_selection_alpha(selection)

    def __calculate_thresholds(self) -> None:
        for selection in self.__selections:
            selection['analysis']['alpha_threshold'] = abs(selection['params']['scale'] - selection['analysis']['estimated_alpha'])

    def __calculate_dispersions(self) -> None:
        for selection in self.__selections:
            selection['analysis']['dispersion'] =

    def generate_selection(self, n_selections: int, size: int) -> None:
        for i in range(n_selections):
            self.__selections.append({
                'rvs': laplace.rvs(loc=self.__beta, scale=self.__alpha, size=size),
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
                }
            })




def calculate_alpha_estimation(selection: ndarray) -> Decimal:
    selection_squared = square_array(selection)
    return Decimal.sqrt((2 * selection.size) / (selection_squared.sum()))


def calculate_alpha_offset(alpha: Decimal, alpha_estimation: Decimal) -> Decimal:
    return alpha - alpha_estimation


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    selection_s = laplace.rvs(loc=beta, scale=alpha, size=size_s)
    selection_m = laplace.rvs(loc=beta, scale=alpha, size=size_m)
    selection_l = laplace.rvs(loc=beta, scale=alpha, size=size_l)
    selection_xl = laplace.rvs(loc=beta, scale=alpha, size=size_xl)
    calculate_alpha_estimation(selection_s)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
