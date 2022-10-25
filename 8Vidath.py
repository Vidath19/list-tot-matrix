def adjacency_list_to_incident_matrix(adjacency_list):
    list_len = len(adjacency_list)
    # Calculate the max number of edges in a graph of n vertices n*(n-1)/2
    max_edges = (list_len * (list_len - 1)) / 2
    incident_matrix = [[0] * list_len for _ in range(max_edges)]
    current_row = 0
    for parent_vertex, vertices in adjacency_list.iteritems():
        for child_vertex in vertices:
            # Since the graph is undirected we can ignore duplicating the edge.
            if child_vertex < parent_vertex:
                continue
            incident_matrix[current_row][parent_vertex] = 1
            incident_matrix[current_row][child_vertex] = 1
            current_row += 1
    return incident_matrix