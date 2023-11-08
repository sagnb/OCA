from collections import deque
import numpy as np
import os.path
import argparse
from argparse import RawTextHelpFormatter

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
    """
    Performs a breadth-first search to find a path in the maze.

    Args:
        maze (list of lists): A two-dimensional array representing the maze.
        start (tuple): The starting maze position.
        end (tuple): The destination maze position.

    Returns:
        A list of positions representing the path from start to end, or an empty list if there is no path.
    """ 

    '''
        :param maze: numpy.ndarray
        :param start_point: np.ndarray
        :param end_point: np.ndarray
    '''
    queue = deque()
    queue.append(start_node)

    while queue:
        current_node = queue.popleft()

        '''
        # Check if the current node is the end node
        # Reconstruct the path from the end to the start
        
        '''

        if current_node.equals(end_node):
            path = []
            current = current_node

            '''
            # Reconstruct the rollback path
            '''
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        movements = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        '''
        # Check possible moves from the current node
        '''
        for movement in movements:
            new_position = (current_node.position[0] + movement[0], current_node.position[1] + movement[1])
            
            '''
            # Check if the new position is not the maze edges and not an obstacle
            '''
            if 0 <= new_position[0] < len(maze) and 0 <= new_position[1] < len(maze[0]) and maze[new_position[0]][new_position[1]] == 0:
                '''
                # Create a new node for the new position and add it to the search queue
                '''
                new_node = Node(current_node, new_position)
                queue.append(new_node)

    return []

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
   
    start = tuple(args.start_point)
    end = tuple(args.end_point)
 
    path = breadth_first_search(maze, start, end)

    print(path)

if __name__ == "__main__":
    main()