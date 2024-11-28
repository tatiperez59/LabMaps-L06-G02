def breadth_first_search(my_graph, source):

    """

    Inicia un recorrido BFS sobre el grafo a partir del vertice source y

    usa la función bfs_vertex(...).

    Params:

        my_graph (adj_list_graph): el grafo a recorrer.

        source: Vertice inicio del recorrido

    Returns (graph_search):

        Estructura con los vértices alcanzables desde el vértice de inicio

    """

    search = {'source':source, 'visited':None}

    search['visited'] = map.new_map(

        num_elements=graph.num_vertices(my_graph),

        load_factor=0.5 )



    # Marcar el vertice source en el mapa search['visited']

    map.put(search["visited"], source, None)



    # Usar la funcion iterativa bfs_vertex(...) para marcar los vertices alcanzables desde el vertice source

    bfs_vertex(search, my_graph, source)



    # Retornar la estructura completa con los vertices alcanzables/marcados.

    return search
