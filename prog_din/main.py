'''https://github.com/sagnb/OCA'''

from argparse import RawTextHelpFormatter
import argparse
import os.path
import tracemalloc
import timeit
import numpy as np

import utils.kohonen


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


def shortest_path(current_indexarr:np.ndarray, max_indexarr:int, matrix:np.ndarray, map:np.ndarray):
    '''
    Return Shortest Path between i and j
    '''
    path = {}
    max_index = max_indexarr[0] * max_indexarr[1] - 1
    current_index = max_indexarr[1] * current_indexarr[0] + current_indexarr[1]
    if map[current_indexarr[0]][current_indexarr[1]] != 1:
        if utils.kohonen.dissimilarity(np.array([0, 0]), current_indexarr, 1) == 1:
            matrix[0][current_index] = 1
        if current_index == 0:
            matrix[current_index][0] = 0
        elif matrix[0][current_index] == np.Inf:
            lst_min = []

            ops = [[0, 1], [-1, 0], [0, -1]]
            for op in ops:
                iarr = current_indexarr + op
                i = max_indexarr[1] * iarr[0] + iarr[1]
                if i < len(matrix) and i > 0 and iarr[0] < len(map) and iarr[1] < len(map[0])  and map[iarr[0]][iarr[1]] != 1:
                    if matrix[i][current_index] == np.Inf:
                        matrix[i][current_index] = 1

                    lst_min.append(matrix[i][current_index] + matrix[0][i])
                    path[matrix[i][current_index] + matrix[0][i]] = i
            matrix[0][current_index] = min(lst_min)
            matrix[current_index][0] = path[matrix[0][current_index]]
        else:
            matrix[current_index][0] = 0

    if current_index != max_index:
        current_index += 1
        current_indexarr = np.array([current_index//max_indexarr[1], current_index%max_indexarr[1]])
        shortest_path(current_indexarr, max_indexarr, matrix, map)


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

    
    time = timeit.timeit(lambda: shortest_path(start, np.array(shape), shortest_matrix, input_matrix), number=1)

    memo = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    # print('caminho:', end=' ')
    # result = tam
    # while result != 0:
    #     print(int(result), end=' ')
    #     result = shortest_matrix[int(result)][0]
    # print(0)

    # my_som.plot_path()

    # total_dist = 0
    # for i, neuron in enumerate(my_som.neurons):
    #     dist = utils.kohonen.dissimilarity(neuron, my_som.neurons[i-1]) if i > 0 else 0
    #     total_dist += dist
    print(f'{shortest_matrix[0][tam-1]}\n{memo}\n{time}\n')
