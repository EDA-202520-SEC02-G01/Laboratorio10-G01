from DataStructures.Map import map_linear_probing as mlp
from DataStructures.Graph import diagraph as G
from DataStructures.Queue import queue as pq
from DataStructures.Graph import dijsktra_structure
import math

def init_structure(graph, source):
    structure = dijkstra_structure.new_dijkstra_structure(source, G.order(graph))
    vertices = G.vertices(graph)
    for i in range(lt.size(vertices)):
        vert = lt.get_element(vertices, i)
        map.put(structure["visited"], vert, {"marked":False, "edge_from":None,"dist_to":math.inf})
    map.put(structure["visited"], source, {"marked":False, "edge_from":None, "dist_to":0})
    pq.insert(structure["pq"], source, 0 )
    return structure

def has_path_to(vertex, structure):
    visited = structure["visited"]

    if mlp.contains(visited, vertex):
        info = mlp.get(visited, vertex)
        if info["marked"] is True:
            return True

    return False
