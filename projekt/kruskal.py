import convert as cv


class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal(edges):
    vertices = cv.read_vertices(edges)
    edges.sort(key=lambda x: x[2])
    MST = []
    V = []
    for v in vertices:
        V.append(Node(v))

    for edge in edges:
        u = edge[0]
        v = edge[1]
        if find(V[u]) != find(V[v]):
            MST.append(edge)
            union(V[u], V[v])
    return MST
