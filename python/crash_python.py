# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 17:46:53 2020

@author: Bast
"""



x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zero = x[0] # equals 0, lists are 0-indexed
one = x[1] # equals 1
nine = x[-1] # equals 9, 'Pythonic' for last element
eight = x[-2] # equals 8, 'Pythonic' for next-to-last element
x[0] = -1 # now x is [-1, 1, 2, 3, ..., 9]

first_three = x[:3] # [-1, 1, 2]
three_to_end = x[3:] # [3, 4, ..., 9]
one_to_four = x[1:5] # [1, 2, 3, 4]
last_three = x[-3:] # [7, 8, 9]
without_first_and_last = x[1:-1] # [1, 2, ..., 8]
copy_of_x = x[:] # [-1, 1, 2, ..., 9]


print(first_three)
print(three_to_end)
print(one_to_four)
print(last_three)
print(without_first_and_last)
print(copy_of_x)

five_to_three = x[5:2:-3] # [5, 4, 3]
print(five_to_three)

test=[1,2]
test.extend([3,4])
print(len(test))


# Tuples
my_liste=[1,2]
my_tuple=(1,2)
my_liste[1]= 3


try:
    my_tuple[1]=3
except TypeError:
    print("Tuple immutables")


def sum_and_product(x, y):
    """
    Calcule la somme et le produit de x et y et renvoie les deux calculs dans un tuple

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return (x + y), (x * y)

sp = sum_and_product(8, 9)
print(sp)
s, p = sum_and_product(8, 9)
print("s: {} p: {}".format(s, p))    

x, y = 1, 2
x, y = y, x

# Dictionaries

empty_dict = {}
empty_dict2 = dict()
grades = {"Joel": 80, "Tim": 95}

joels_grade = grades["Joel"]
print(joels_grade)



try:
    print(grades["Bastien"])
except KeyError:
    print("Clé introuvable")
    
joel_has_grade = "Joel" in grades
print(joel_has_grade)
bastien_has_grade = "Bastien" in grades
print(bastien_has_grade)

joels_grade = grades.get("Joel", 0) # equals 80
kates_grade = grades.get("Kate", 0) # equals 0
no_ones_grade = grades.get("No One") # default is None


print(joels_grade)
print(kates_grade)
print(no_ones_grade)


tweet = {
"user" : "joelgrus",
"text" : "Data Science is Awesome",
"retweet_count" : 100,
"hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()
print(tweet_keys)

tweet_values = tweet.values()
print(tweet_values)

tweet_items = tweet.items()
print(tweet_items)



from collections import defaultdict

word_counts = defaultdict(int)
document = ["Bonjour","je", "suis", "un", "document"]

for word in document:
    word_counts[word] += 1


dd_list = defaultdict(list)
dd_list[2].append(1)

dd_list = defaultdict(list) # list() produces an empty list
dd_list[2].append(1) # now dd_list contains {2: [1]}
print(dd_list)


from collections import Counter

words_counts = Counter(document)

for word, count in words_counts.most_common(10):
    print(word, count)


for x in range(5, 10):
    print(x)
    
    
    

class CountingClicker:
    """Class docstring example"""
    
    
    def __init__(self, count = 0):
        self.count = count
        
    
    def click(self, num_time = 1):
        self.count += num_time
        
    def read(self):
        return self.count
    
    def reset(self):
        self.count = 0
    

        
        
clicker1 = CountingClicker()
clicker2 = CountingClicker(100)
clicker3 = CountingClicker(count=100)


assert clicker1.read() == 0, "clicker should start with count 0"
clicker1.click()
clicker1.click()
assert clicker1.read() == 2, "clicker should have count 2"
clicker1.reset()
assert clicker1.read() == 0, "after reset, clicker should be 0"

# A subclass of CountingClicker
class NoResetClicker(CountingClicker):
    
    def reset(self):
        pass


clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1



def generator_range(n):
    i = 0
    print("je")
    while i < n:
        yield i
        i += 1

generator_range(10)

for i in generator_range(10):
    print(f"i: {i}")
    

names = ["Alice", "Bob", "Charlie", "Debbie"]
# not Pythonic
for i in range(len(names)):
    print(f"name {i} is {names[i]}")
# also not Pythonic
i = 0
for name in names:
    print(f"name {i} is {names[i]}")
    i += 1
# Pythonic
for i, name in enumerate(names):
    print(f"name {i} is {name}")



import re

re_examples = re.search("a", "cat")
print(re_examples)

re_2 = re.split("[ar]", "carbs")
print(re_2)



def doubler(f):
    # Here we define a new function that keeps a reference to f
    def g(x,y):
        return 2 * f(x,y)
    # And return that new function
    return g


def f1(x,y):
    return x + 1

g = doubler(f1)

print(g(3,2))


