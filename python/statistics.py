# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:56:32 2020

@author: Bast
"""

from typing import List
from collections import Counter
from algebra import sum_of_squares
import math
from algebra import dot


def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)


def _median_odd(xs: List[float]) -> float:
    return sorted(xs)[len(xs) // 2]


def _median_even(xs: List[float]) -> float:
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2
    return(sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

def median(v: List[float]) -> float:
   return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


def quantile(xs: List[float], p: float) -> float:
    if p == 0.5:
        print("Mediane : ", median(xs))
    p_index = int(p * len(xs))
    print(p_index)
    return sorted(xs)[p_index]


print(quantile([10, 25, 30, 50, 70], 0.5))

def mode(x: List[float]) -> float:
    counts = Counter(x)
    max_count = max(counts.values)
    return [x_i for x_i, count in counts.items() if count == max_count]

def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)


def de_mean(xs: List[float])  -> float:
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) -> float:
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(xs: List[float]) -> float:
    return math.sqrt(variance(xs))

def interquartile_range(xs: List[float]) -> float:
    return quantile(xs, 0.75) - quantile(xs, 0.25)

def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys)
    return dot((de_mean(xs), de_mean(ys) / (len(xs) - 1)))


def correlation(xs: List[float], ys: List[float]) -> float:
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x * stdev_y
    else:
        return 0
    



