from DataStructures.Map import map_linear_probing as mlp
from DataStructures.Graph import diagraph as G
from DataStructures.Queue import queue as q

def bfs_vertex(my_graph, source, visited_ht):
    queue = q.new_queue()
    q.enqueue(queue, source)

    visited_ht[source]["marked"] = True
    visited_ht[source]["edge_from"] = None
    visited_ht[source]["dist_to"] = 0

    while not q.is_empty(queue):
        vertex = q.dequeue(queue)
        adj = G.edges_vertex(my_graph, vertex)

        for edge in adj:
            w = edge["vertex"]

            if not mlp.contains(visited_ht, w):
                mlp.put(visited_ht, w, {
                    "marked": True,
                    "edge_from": vertex,
                    "dist_to": visited_ht[vertex]["dist_to"] + 1
                })

                q.enqueue(queue, w)

    return visited_ht







