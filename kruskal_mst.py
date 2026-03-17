#!/usr/bin/env python
# coding: utf-8

# In[1]:

def kruskal():
    num_of_ver = int(input("Enter the number of vertex: "))
    num_of_eg = int(input("Enter the number of edges: "))
    edges = []
    print("Enter (weight vertex1 vertex2):")
    for _ in range(num_of_eg):
        data = input().split()
        edges.append((float(data[0]), data[1], data[2]))
    sorted_edges = sorted(edges, key = lambda x: x[0])

    connections = {}

    def get_root(vertex):
        if vertex not in connections: 
            connections[vertex] = vertex
        if connections[vertex] == vertex: 
            return vertex
        connections[vertex] = get_root(connections[vertex])
        return connections[vertex]

    def join_sets(a, b):
        root_a, root_b = get_root(a), get_root(b)
        if root_a != root_b:
            connections[root_a] = root_b
            return True
        return False

    def join_groups(vertex_a, vertex_b):
        head_a = get_root(vertex_a)
        head_b = get_root(vertex_b)
        if head_a != head_b:
            connections[head_a] = head_b
            return True
        return False
    mst = []
    total_weight = 0

    for w, v1, v2 in sorted_edges:
        if join_sets(v1, v2):
            mst.append((v1, v2, w))
            total_weight += w
            if len(mst) == num_of_ver - 1:
                break

    print("\nMST:")
    for v1, v2, w in mst:
        print(f"{v1} - {v2}")
    print(f"Total distance: {total_weight}")
    input("Press Enter to close the program...")
# In[2]:
kruskal()
# In[ ]:
