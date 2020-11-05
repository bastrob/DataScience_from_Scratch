# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 18:58:41 2020

@author: Bast
"""

from typing import List

Vector = List[float]

def add(v: Vector, w: Vector) -> Vector:
    """
    Adds corresponding elements

    Parameters
    ----------
    v : Vector
        DESCRIPTION.
    w : Vector
        DESCRIPTION.

    Returns
    -------
    Vector
        DESCRIPTION.

    """
    
    assert len(v) == len(w), "Vectors must be same length"
    
    return [v + w for v, w in zip(v, w)]

assert add([1, 2, 3], [5, 8, 10]) == [6, 10, 13]

def substract(v: Vector, w: Vector) -> Vector:
    
    assert len(v) == len(w), "Vectors must be same length"
    
    return [v - w for v, w in zip(v, w)]

assert substract([10,5,1], [12,9,5]) == [-2, -4, -4]


def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "no vectors provided"
    
    # check vectors size
    size_vector = len(vectors[0])
    
    assert [len(vector) == size_vector for vector in vectors], "different sizes!"
    
    #i th element of all vector = i th element of new vector
    
    return [sum(vector[i] for vector in vectors) for i in range(size_vector)]
    
assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]
    

def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

def dot(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "must be same length"
    
    # v_i * w_i ... v_n * w_n
    
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [5, 5, 5]) == 30

def sum_of_squares(v: Vector) -> float:
    """
    Returns v_1 * v_1 + ... + v_n * v_n

    Parameters
    ----------
    v : Vector
        DESCRIPTION.

    Returns
    -------
    float
        DESCRIPTION.

    """
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14 # 1 * 1 + 2 * 2 + 3 * 3

import math

def magnitude(v: Vector) -> Vector:
    return math.sqrt(sum_of_squares(v))

assert magnitude([4, 3]) == 5

def squared_distance(v: Vector, w: Vector) -> Vector:
    return sum_of_squares(substract(v, w))

def distance(v: Vector, w: Vector) -> Vector:
    return math.sqrt(squared_distance(v, w))


def distance_cleaner(v: Vector, w: Vector) -> Vector:
    return magnitude(substract(v, w))


Matrix = List[List[float]]

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],
     [6, 7]]


print(len(B))
print(len(B[2]))

from typing import Tuple

def shape(A: Matrix) -> Tuple[int, int]:
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    
    return num_rows, num_cols

assert shape([[1, 2], [5, 6]]) == (2, 2)

def get_row(A: Matrix, i: int) -> Vector:
    return A[i]

def get_col(A: Matrix, j: int) -> Vector:
    return [A_i[j] for A_i in A]


from typing import Callable

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    return [[entry_fn(i, j)
             for j in range(num_cols)]
             for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)