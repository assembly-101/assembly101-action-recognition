import sys
sys.path.insert(0, '')
sys.path.extend(['../'])

import numpy as np

from graph import tools

num_node = 21
self_link = [(i, i) for i in range(num_node)]
inward = [
    (5, 17), (17, 18), (18, 19), (19, 4),  # pinky
    (5, 14), (14, 15), (15, 16), (16, 3),  # ring
    (5, 11), (11, 12), (12, 13), (13, 2),  # middle
    (5, 8), (8, 9), (9, 10), (10, 1),  # index
    (5, 6), (6, 7), (7, 0),  # thumb
    (6, 8), (8, 11), (11, 14), (14, 17),  # palm
                    ]
outward = [(j, i) for (i, j) in inward]
neighbor = inward + outward



class AdjMatrixGraph:
    def __init__(self, *args, **kwargs):
        self.edges = neighbor
        self.num_nodes = num_node
        self.self_loops = [(i, i) for i in range(self.num_nodes)]
        self.A_binary = tools.get_adjacency_matrix(self.edges, self.num_nodes)
        self.A_binary_with_I = tools.get_adjacency_matrix(self.edges + self.self_loops, self.num_nodes)
        self.A = tools.normalize_adjacency_matrix(self.A_binary)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    graph = AdjMatrixGraph()
    A, A_binary, A_binary_with_I = graph.A, graph.A_binary, graph.A_binary_with_I
    f, ax = plt.subplots(1, 3)
    ax[0].imshow(A_binary_with_I, cmap='gray')
    ax[1].imshow(A_binary, cmap='gray')
    ax[2].imshow(A, cmap='gray')
    plt.show()
    print(A_binary_with_I.shape, A_binary.shape, A.shape)
