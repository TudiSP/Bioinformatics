from ete3 import Tree
from E7A import calculate_leaf_distances
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # we load a tree
    t = Tree('((((H:1,K:1)D:2,(F:1,I:0.5)G:1)B:2,E:3)A:23,((L:2,(N:1,Q:0.1)O:4)J:5,(P:2,S:2)M:1)C:7);', format=1)
    #
    t2 = Tree("((A:1,B:1)E:2, (C:1,D:1)F:2);", format=1)
    #
    tex = Tree('((Chimp:1,Human:2):3,(Seal:2, Whale:0):0);', format=1)

    distance_matrix = calculate_leaf_distances(tex, verbose=True)