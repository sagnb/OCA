'''https://github.com/sagnb/OCA'''

from argparse import RawTextHelpFormatter
import argparse
import os.path
import tracemalloc
import timeit
import numpy as np


def args():
    '''
    Return args
    
    :return arguments passed to the program: argparse.Namespace
    '''
    result = argparse.ArgumentParser(
        description='Motion Planning Program using SOMs (Self Organizing Maps)',
        formatter_class=RawTextHelpFormatter
    )
    result.add_argument('input', type=str, help='input map name')
    result.add_argument(
        '-s',
        '--start',
        dest='start_point',
        type=int,
        help='startposition in matrix',
        nargs='+'
    )
    result.add_argument(
        '-e'
        '--end',
        dest='end_point',
        type=int,
        help='end position in matrix',
        nargs='+'
    )
    return result.parse_args()


def dissimilarity(a:np.ndarray, b:np.ndarray, p:int=2)->np.float64:
    '''
    Return the dissimilarity between a and b
    
    :param a: numpy.ndarray
    :param b: numpy.ndarray
    :param p: int
    
    :return dissimilarity: numpy.float64
    '''
    result = sum(
        [pow(abs(i - j), p) for i, j in zip(a, b)]
    )
    return pow(result, 1/p)


def shortest_path(
    current_indexarr:np.ndarray,
    max_indexarr:np.ndarray,
    matrix:np.ndarray,
    input_map:np.ndarray
):
    '''
    :param current_indexarr: numpy.ndarray
    :param max_indexarr: numpy.ndarray
    :param matrix: numpy.ndarray
    :param input_map: numpy.ndarray
    
    Return Shortest Path between i and j
    '''
    while True:
        path = {}
        max_index = max_indexarr[0] * max_indexarr[1] - 1
        current_index = max_indexarr[1] * current_indexarr[0] + current_indexarr[1]
        if input_map[current_indexarr[0]][current_indexarr[1]] != 1:
            if dissimilarity(np.array([0, 0]), current_indexarr, 1) == 1:
                matrix[0][current_index] = 1
            if current_index == 0:
                matrix[current_index][0] = 0
            elif matrix[0][current_index] == np.Inf:
                lst_min = []

                ops = [[0, 1], [-1, 0], [0, -1]]
                for op in ops:
                    iarr = current_indexarr + op
                    i = max_indexarr[1] * iarr[0] + iarr[1]
                    if i < len(matrix) and i > 0 and iarr[0] < len(input_map) and iarr[1] < len(input_map[0])  and input_map[iarr[0]][iarr[1]] != 1:
                        if matrix[i][current_index] == np.Inf:
                            matrix[i][current_index] = 1

                        lst_min.append(matrix[i][current_index] + matrix[0][i])
                        path[matrix[i][current_index] + matrix[0][i]] = i
                if lst_min:
                    matrix[0][current_index] = min(lst_min)
                    matrix[current_index][0] = path[matrix[0][current_index]]
            else:
                matrix[current_index][0] = 0

        if current_index != max_index:
            current_index += 1
            current_indexarr = np.array(
                [current_index//max_indexarr[1],
                 current_index%max_indexarr[1]]
            )
        else:
            break


if __name__ == '__main__':
    param = args()
    start = param.start_point
    end = param.end_point
    input_matrix = np.zeros((10, 10))

    if os.path.isfile(param.input):
        input_matrix = np.loadtxt(param.input)

    if start is None:
        start = np.array([0 for i in input_matrix.shape])

    if end is None:
        end = np.array([i-1 for i in input_matrix.shape])

    shape = input_matrix.shape
    tam = shape[0] * shape[1]

    shortest_matrix = np.ones((tam, tam), dtype=np.float64) * np.Inf

    tracemalloc.start()


    time = timeit.timeit(
        lambda: shortest_path(start, np.array(shape), shortest_matrix, input_matrix),
        number=1
    )

    memo = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    print(f'{shortest_matrix[0][tam-1]}\n{memo}\n{time}\n')
