'''Kohonen Map or SOM(Self Organizing Maps)'''

import math
import numpy as np
import matplotlib.pylab as plt


def dissimilarity(a:np.ndarray, b:np.ndarray, p:int=2)->np.float64:
    '''
    Return the dissimilarity between a and b
    
    :param a: numpy.ndarray
    :param b: numpy.ndarray
    
    :return dissimilarity: numpy.float64
    '''
    result = sum(
        [pow(abs(i - j), p) for i, j in zip(a, b)]
    )
    return pow(result, 1/p)


def vet(a:np.ndarray, b:np.ndarray)->np.ndarray:
    '''
    Generates vector between a and b
    
    :param a: numpy.ndarray
    :param b: numpy.ndarray
    
    :return vector: numpy.ndarray
    '''
    return np.array([j - i for i, j in zip(a, b)])


def gaussian(
        current_index:int, winner_index:int,
        current_time:int, max_time:int,
        max_sigma:float
    )->float:
    '''
    Returns the result of the Gaussian function taking into account
    the topology of the winning neuron and the neuron currently
    being recalculated
    
    :param current_index: int
    :param winner_index: int
    :param current_time: int
    :param max_time: int
    :param max_sigma: float
    
    :return Gaussian value: float
    '''
    sigma = max_sigma * (1.0 - current_time / max_time)
    sigma *= ((1.0 / 1.5) ** (current_time / max_time))
    nb = (current_index - winner_index) ** 2.0
    return (1.0 - current_time / max_time) * math.exp(-nb / (2.0 * (sigma ** 2.0)))


class SOM:
    '''
    Self Organizing Maps
    '''
    def __init__(
            self,
            input_matrix:np.ndarray,
            start_point:np.ndarray,
            end_point:np.ndarray,
        ):
        '''
        :param input_matrix: numpy.ndarray
        :param start_point: numpy.ndarray
        :param end_point: np.ndarray
        '''
        self.input_matrix = input_matrix
        self.winner_index = -1.5
        self.start_point = start_point
        self.end_point = end_point
        self.neurons = np.zeros((
            np.int64(dissimilarity(start_point, end_point, 1)),
            input_matrix.ndim
        ))

        self.neurons[0] = start_point
        self.neurons[len(self.neurons)-1] = end_point

        steps = vet(start_point, end_point)/float(len(self.neurons))
        aux = steps.copy()

        for index in range(1, len(self.neurons)-1):
            for dim in range(input_matrix.ndim):
                self.neurons[index][dim] = start_point[dim]#int(aux[dim])
                aux[dim] += steps[dim]

    def fit(self, max_time:int, max_sigma:float):
        '''
        Adjust neuron weights
        
        :param max_time: int
        :param max_sigma: float
        '''
        for current_time in range(max_time):
            seed = np.random.randint(
                1, self.input_matrix.shape
            )
            # seed = self.start_point if current_time%2==0 else self.end_point

            eta = 0.5 if current_time < max_time/2.0 else 0.05

            factor = 1
            if self.input_matrix[seed[0]][seed[1]] == 1:
                factor = -2
                # continue

            self.find_winner(seed)

            for index, neuron in enumerate(self.neurons):
                if index == 0 or index == len(self.neurons) -1:
                    continue
                vet_seed = vet(neuron, seed) * factor
                gauss = gaussian(
                    index, self.winner_index, current_time,
                    max_time, max_sigma
                )
                for dim in range(self.input_matrix.ndim):
                    self.neurons[index][dim] += gauss * eta * vet_seed[dim]

    def find_winner(self, seed:np.ndarray):
        '''
        Find winner in neurons vector
        
        :param seed: numpy.ndarray
        '''
        seed_dist = math.inf
        for index, neuron in enumerate(self.neurons):
            new_dist = dissimilarity(seed, neuron)
            if new_dist < seed_dist:
                seed_dist = new_dist
                self.winner_index = index

    def plot_path(self):
        '''
        Plot the fit path using matplotlib
        '''
        plt.plot(self.neurons[:, 0], self.neurons[:, 1])
        for i, row in enumerate(self.input_matrix):
            for j, point in enumerate(row):
                if point == 1:
                    plt.scatter(
                        i,
                        j,
                        marker='*',
                        c='green'
                    )
        plt.show()
