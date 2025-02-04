#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import uniform as uniform_dist
from scipy.stats import norm as norm_dist
from scipy.stats import beta as beta_dist


def central_limit(rvs, n, length):
    rv_mean = np.zeros(length)
    for i in range(n):
        rv = rvs(size=length)
        rv_mean = rv_mean + rv
    rv_mean = rv_mean / n
    gaussian_params = norm_dist.fit(rv_mean)
    gaussian = norm_dist(gaussian_params[0], gaussian_params[1])
    return rv_mean, gaussian


def main():
    fig = plt.figure()
    x = np.linspace(0, 1, 100)
    sizes = [1, 2, 20, 50]
    fig_row, fig_col = 2, 4

    # Mean of i.i.d uniform
    for i, n in enumerate(sizes):
        ax = fig.add_subplot(fig_row, fig_col, i + 1)
        data, gaussian = central_limit(uniform_dist.rvs, n, 1000)
        ax.hist(data, bins=20, normed=True, alpha=0.7)
        plt.plot(x, gaussian.pdf(x), 'r')
        plt.title('n={0}'.format(n))

    # Mean of i.i.d beta(1, 2)
    for i, n in enumerate(sizes):
        ax = fig.add_subplot(fig_row, fig_col, i + fig_col + 1)
        data, gaussian = central_limit(beta_dist(1, 2).rvs, n, 1000)
        ax.hist(data, bins=20, normed=True, alpha=0.7)
        plt.plot(x, gaussian.pdf(x), 'r')
        plt.title('n={0}'.format(n))

    plt.show()

if __name__ == '__main__':
    main()
