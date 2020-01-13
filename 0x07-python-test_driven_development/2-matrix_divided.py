#!/usr/bin/python3
def matrix_divided(matrix, div):
    Error = "matrix must be a matrix (list of lists) of integers/floats"
    LenError = "Each row of the matrix must have the same size"
    new = [[]]

    if type(matrix) is not list:
        raise TypeError(Eror)

    length = len(matrix[0])
    for i in matrix:
        if length != len(i):
            raise TypeError("LenError")

        for j in range(len(i)):
            if type(i[j]) != int and type(i[j]) != float:
                raise TypeError(Error)

            if type(div) != int and type(div) != float:
                raise TypeError("div must be a number")

    return [[float("{0:.2f}".format(j/div)) for j in i] for i in matrix]
            
