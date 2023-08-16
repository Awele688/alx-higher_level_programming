#!/usr/bin/python3
""" function that computes the square value of all integers of a matrix."""


def square_matrix_simple(matrix=[]):
    novel_matrix = matrix.copy()

    for j in range(len(matrix)):
        novel_matrix[j] = list(map(lambda x: x**2, matrix[j]))

    return (novel_matrix)
