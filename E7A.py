from ete3 import Tree
import numpy as np

# Distances between leaves problem
def calculate_leaf_distances(tree : Tree, verbose=False):
    n = len(tree)
    distances = np.zeros((n, n), dtype=int)
    leaves = [leaf for leaf in tree if leaf.is_leaf()]
    for i, leaf1 in enumerate(leaves):
        for j, leaf2 in enumerate(leaves):
                if i >= j:
                    distance = tree.get_distance(leaf1, leaf2)
                    distances[i, j] = distance

    if verbose:
        print(tree.get_leaf_names())
        tree.show()
        print(distances)

    return distances