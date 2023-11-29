import numpy as np
import pandas as pd


if __name__ == '__main__':
    dim = []
    difficulty = []
    dist = []
    memo = []
    time = []
    algorithm = []
    index_map = []

    for i in [10, 20, 50]:
        for j in ['F', 'M', 'D']:
            for k in ['bfs', 'kohonen', 'prog_din']:
                for l in range(1, 11):
                    with open(f'generate/{i}x{i}{j}/result{k}map{l}.txt', encoding='utf-8') as file:
                        dim.append(i)
                        difficulty.append(j)
                        algorithm.append(k)
                        index_map.append(l)
                        for m, line in enumerate(file):
                            if m == 0:
                                dist.append(np.float64(line))
                            elif m == 1:
                                memo.append(np.float64(line))
                            elif m == 2:
                                time.append(np.float64(line))
                            else:
                                continue
    pd.DataFrame({
        'algorithm': algorithm,
        'dim': dim,
        'difficulty': difficulty,
        'index_map': index_map,
        'distance': dist,
        'ram': memo,
        'time': time
    }).to_csv('metrics.csv')
