def matrix_to_edges(_matrix):
    edges = []
    for i in range(len(_matrix)):
        for j in range(i):
            if _matrix[i][j] != 0:
                edges.append((i, j, _matrix[i][j]))
    return edges


def edges_to_matrix(_edges):
    vertices = read_vertices(_edges)
    result = []
    for i in range(len(vertices)):
        result.append([])
        for _ in vertices:
            result[i].append(0)
    for edge in _edges:
        result[edge[0]][edge[1]] = edge[2]
        result[edge[1]][edge[0]] = edge[2]
    return result


def list_to_edges(_list):
    edges = []
    for i in range(len(_list)):
        for j in range(len(_list[i])):
            if _list[i][j][0] > i:
                edges.append((i, _list[i][j][0], _list[i][j][1]))
    return edges


def edges_to_list(_edges):
    vertices = read_vertices(_edges)
    result = []
    for i in range(len(vertices)):
        result.append([])
        for edge in _edges:
            if edge[0] == vertices[i]:
                result[i].append((edge[1], edge[2]))
            if edge[1] == vertices[i]:
                result[i].append((edge[0], edge[2]))
    return result


def read_vertices(_edges):
    vertices = []
    for edge in _edges:
        if edge[0] not in vertices:
            vertices.append(edge[0])
        if edge[1] not in vertices:
            vertices.append(edge[1])
    return vertices
