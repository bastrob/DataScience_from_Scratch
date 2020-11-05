# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 16:52:01 2020

@author: Bast
"""

from matplotlib import pyplot as plt


# Simple plot
# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# plt.plot(years, gdp, color="green", marker="o", linestyle="solid")

# plt.legend("Nominal GDP")



# Bar chart
# movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
# num_oscars = [5, 11, 3, 8, 10]


# plt.bar(range(len(movies)), num_oscars)

# plt.title("My Favorites Movies")
# plt.ylabel("# of Academy rewards")

# # xticks , labels
# plt.xticks(range(len(movies)), movies)
# plt.xlabel(("Movies"))

from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Bucket grades by decile, but put 100 in with the 90s
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

print(histogram)