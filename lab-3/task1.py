from scipy.stats import norm, t as t_student, f
import numpy

def f_test_variance(size1, size2):
    return (2 * pow(size2 - 1, 2) * (size1 + size2 - 4)) / ((size1 - 1) * pow(size2 - 3, 2) * (size2 - 5))

if __name__ == '__main__':
    mu_1 = 0
    mu_2 = 0
    D_1 = 2
    D_2 = 1
    alpha = 0.05
    sizes = [25, 10000]
    n_repeats = 1000
    tau = D_1 / D_2
    for size in sizes:
        alpha_contains_counter = 0
        alpha_exceeds_counter = 0
        for i in range(n_repeats):
            selection_1 = norm.rvs(loc=mu_1, scale=numpy.sqrt(D_1), size=size)
            selection_2 = norm.rvs(loc=mu_2, scale=numpy.sqrt(D_2), size=size)
            threshold_left = (selection_1.var() / selection_2.var()) * f.ppf(alpha / 2, size - 1, size - 1)
            threshold_right = (selection_1.var() / selection_2.var()) * f.ppf(1 - alpha / 2, size - 1, size - 1)
            if tau > threshold_left and tau < threshold_right:
                alpha_contains_counter = alpha_contains_counter + 1
            else:
                alpha_exceeds_counter = alpha_exceeds_counter + 1
        print("n = m = " + str(size) + ", " + str((1 - alpha) * 100) + "% covered " + str(alpha_contains_counter) + ", excluded " + str(alpha_exceeds_counter))