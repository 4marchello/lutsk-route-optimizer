#!/usr/bin/env python
# coding: utf-8

# 0 - КАМІНЬ-КАШИРСЬКИЙ НАРОДНИЙ КРАЄЗНАВЧИЙ МУЗЕЙ
# 1 - Любомльський краєзнавчий музей
# 2 - Садиба Косачів
# 3 - Волинський краєзнавчий музей
# 4 - Лобненський музей партизанської Слави
# 5 - Музей флори та фауни Шацького лісового коледжу
# 6 - Володимирський історичний музей ім О. М. Дверницького

# In[3]:


import numpy as np
INF = np.inf
START_NODE = int(input("Enter start point: "))
INF = np.inf
graph = [
    #1      2    3     4    5     6    7
    [0,    INF, 61.8, INF, 60.6, INF, INF], # 1 
    [INF,  0,   59,   INF, INF,  32,  52],  # 2 
    [61.8, 59,  0,    66,  INF,  93,  60],  # 3 
    [INF,  INF, 66,   0,   151.1,INF, 77],  # 4 
    [60.6, INF, INF,  151.1,0,   INF, INF], # 5 
    [INF,  32,  93,   INF, INF,  0,   INF], # 6 
    [INF,  52,  60,   77,  INF,  INF, 0]    # 7 
]


def dijkstra(graph, start_node_index):
    N = len(graph)
    distances = [INF] * N
    visited = [False] * N
    predecessors = [-1] * N 
    distances[start_node_index] = 0

    for _ in range(N):
        min_dist = INF
        u = -1 

        for i in range(N):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        for v in range(N):
            weight = graph[u][v]
            if weight != INF: 
                new_dist = distances[u] + weight
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    predecessors[v] = u 

    return distances, predecessors

def reconstruct_path(predecessors, start_node, end_node):
    path = []
    current = end_node

    while current != -1:
        path.append(current)
        if current == start_node:
            break
        current = predecessors[current]

    path.reverse()
    if not path or path[0] != start_node:
         return []
    return path


def dijkstra_all_pairs(graph):
    N = len(graph)
    dist_matrix = np.zeros((N, N))
    predecessor_maps = []

    for i in range(N):
        distances, predecessors = dijkstra(graph, i)
        dist_matrix[i] = distances
        predecessor_maps.append(predecessors)

    return dist_matrix, predecessor_maps


def tsp(dist_matrix, predecessor_maps, start_node_index):
    N = len(dist_matrix)
    visited_major = [False] * N 

    route = [start_node_index]
    visited_major[start_node_index] = True

    current_major_node = start_node_index
    total_distance = 0.0

    for _ in range(N - 1):
        min_dist = INF
        nearest_neighbor = -1

        for next_node in range(N):
            if not visited_major[next_node]:
                distance = dist_matrix[current_major_node, next_node]

                if distance < min_dist:
                    min_dist = distance
                    nearest_neighbor = next_node

        if nearest_neighbor != -1:

            predecessors = predecessor_maps[current_major_node]
            path_segment = reconstruct_path(predecessors, current_major_node, nearest_neighbor)

            if len(path_segment) > 1:
                route.extend(path_segment[1:])

            visited_major[nearest_neighbor] = True
            total_distance += min_dist
            current_major_node = nearest_neighbor 
        else:
            break 

    if route and route[-1] != start_node_index:
        distance_to_start = dist_matrix[current_major_node, start_node_index]
        total_distance += distance_to_start

        predecessors = predecessor_maps[current_major_node]
        path_segment = reconstruct_path(predecessors, current_major_node, start_node_index)

        if len(path_segment) > 1:
            route.extend(path_segment[1:])

    return route, total_distance
shortest_dist_matrix, predecessor_maps = dijkstra_all_pairs(graph)
route_indices, total_distance = tsp(shortest_dist_matrix, predecessor_maps, START_NODE)
print(f"\n Optimized route (start and end at node  {START_NODE}):")
print(f"Route: {' -> '.join(map(str, route_indices))}")
print(f"Total route length: {total_distance:.2f} km.")
input("Press Enter to close the program...")

# In[ ]:




