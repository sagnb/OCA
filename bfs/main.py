from collections import deque
import numpy as np
import os.path
import argparse
from argparse import RawTextHelpFormatter
import tracemalloc
import timeit

class Node:
    def __init__(self, parent=None, position=None):
        """
        Creates a new node in the search tree.

        Args:
            parent: The parent node of this node.
            position: The position in the maze associated with this node.
        """
        self.parent = parent
        self.position = position
    def equals(self, other_node):
        """
        Checks if this node is equal to another node based on their positions.

        Args:
            other_node: The other node to be compared.

        Returns:
            True if the positions of the nodes are equal, False otherwise.
        """
        return self.position == other_node.position

def breadth_first_search(maze, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end)

    queue = deque()
    visited = set()  # Conjunto para manter o controle dos nós visitados
    queue.append(start_node)
    visited.add(start_node.position)

    while queue:
        current_node = queue.popleft()

        # Reconstruct the path from the end to the start
        if current_node.equals(end_node):
            path = []
            current = current_node

            while current is not None:
                path.append(current.position)
                current = current.parent

            # return path[::-1]
            print(len(path[::-1])-1)
            return

        movements = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        '''
        # Check possible moves from the current node
        '''
        for movement in movements:
            new_position = (current_node.position[0] + movement[0], current_node.position[1] + movement[1])
            '''
            # Check if the new position is not the maze edges and not an obstacle
            '''
            if (
                0 <= new_position[0] < len(maze)
                and 0 <= new_position[1] < len(maze[0])
                and maze[new_position[0]][new_position[1]] == 0
                and new_position not in visited
            ):
                '''
                # Create a new node for the new position and add it to the search queue
                '''
                new_node = Node(current_node, new_position)
                queue.append(new_node)
                visited.add(new_position)

    # return []
    print(0)
    return

def get_args():
  '''
    Return args
    
    :return arguments passed to the program: argparse.Namespace
    '''
  
  args = argparse.ArgumentParser(
    description='Motion Planning Program using BFS (Breadth-First Search)',
    formatter_class=RawTextHelpFormatter
  )
  args.add_argument('input', type=str, help='input map name')
  args.add_argument(
    '-s',
    '--start',
    dest='start_point',
    type=int,
    help='startposition in matrix',
    nargs='+'
  )
  args.add_argument(
    '-e',
    '--end',
    dest='end_point',
    type=int,
    help='end position in matrix',
    nargs='+'
  )
  return args.parse_args()

def main():
    args=get_args()

    if os.path.isfile(args.input):
        maze = np.loadtxt(args.input)
    else:
        maze = np.zeros((10, 10))
   
    start = args.start_point
    end = args.end_point
    
    if start is None:
        start = [0 for i in maze.shape]

    if end is None:
        end = [i-1 for i in maze.shape]
    
    start = tuple(start)
    end = tuple(end)

    if start and (maze[start[0]][start[1]] == 1):
        # print("Start position is a blocked position on the maze.")
        print("0\n0\n0")
        return
    elif end and (maze[end[0]][end[1]] == 1):
        # print("End position is a blocked position on the maze.")
        print("0\n0\n0")
        return
    else:
        # path = breadth_first_search(maze, start, end)
        tracemalloc.start()
        time = timeit.timeit(lambda: breadth_first_search(maze, start, end), number=1)
        memo = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        print(f'{memo}\n{time}\n')
        # if not path:
        #     print("No path found.")
        # else:
        #     print("Path:", path)

if __name__ == "__main__":
    main()