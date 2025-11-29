from DataStructures.Map import map_linear_probing as mlp
from DataStructures.Graph import diagraph as G
from DataStructures.Queue import queue as q


def has_path_to(vertex, structure):
    visited = structure["visited"]

    if mlp.contains(visited, vertex):
        info = mlp.get(visited, vertex)
        if info["marked"] is True:
            return True

    return False
