from scipy.stats import geom, norm
import numpy

def f_test_variance(size1, size2):
    return (2 * pow(size2 - 1, 2) * (size1 + size2 - 4)) / ((size1 - 1) * pow(size2 - 3, 2) * (size2 - 5))

if __name__ == '__main__':
    p = 0.7
    alpha = 0.05
    sizes = [25, 10000]
    n_repeats = 1000
    for size in sizes:
        alpha_contains_counter = 0
        alpha_exceeds_counter = 0
        for i in range(n_repeats):
            selection = geom.rvs(p, size=size)
            N = norm.ppf(q=1-alpha/2)
            left_limit = 1/selection.sum() * (-N * numpy.sqrt(size * (1-p)) + size)
            right_limit = 1/selection.sum() * (N * numpy.sqrt(size * (1-p)) + size)
            if p > left_limit and p < right_limit:
                alpha_contains_counter = alpha_contains_counter + 1
            else:
                alpha_exceeds_counter = alpha_exceeds_counter + 1
        print("n = " + str(size) + ", " + str((1-alpha) * 100) + "% covered " + str(alpha_contains_counter) + ", excluded " + str(alpha_exceeds_counter))