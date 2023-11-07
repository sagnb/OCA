'''https://github.com/sagnb/OCA'''

from argparse import RawTextHelpFormatter
import argparse
import os.path
import numpy as np

import som.kohonen


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

    som = som.kohonen.SOM(input_matrix, start, end)
    som.fit(200000, 100)
    som.plot_path()
