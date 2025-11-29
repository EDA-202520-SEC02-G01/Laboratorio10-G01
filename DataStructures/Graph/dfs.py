from DataStructures.Map import map_linear_probing as mlp
from DataStructures.Graph import diagraph as G
from DataStructures.Stack import stack as st

def dfs(my_graph, source):
    
    visited_ht = mlp.new_map(num_elements=G.order(my_graph), load_factor=0.5 )
    mlp.put(visited_ht, source, {'marked': True, 'edge_from': None})
    dfs_vertex(my_graph, source, visited_ht)
    return visited_ht

def has_path_to(key_v, visited_map):
    return mlp.contains(visited_map, key_v)
    
def path_to(vertex, visited_ht):
    
    if vertex not in visited_ht["marked"]:
        return None

    path = st.new_stack()

    while vertex is not None:
        st.push(path, vertex)
        vertex = visited_ht["edge_to"].get(vertex, None)

    return path
