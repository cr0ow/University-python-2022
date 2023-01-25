from convert import read_vertices


def load_from_file(filename):
    result = []
    file = open(filename, "r")
    vertices = int(file.readline())
    for i in range(int(file.readline())):
        line = file.readline().split()
        result.append((int(line[0]), int(line[1]), int(line[2])))
    file.close()
    return result, vertices


def save_to_file(graph, filename):
    file = open(filename, "w")
    file.write(str(len(read_vertices(graph))) + '\n')
    file.write(str(len(graph)) + '\n')
    for edge in graph:
        file.write(str(edge[0]) + ' ' + str(edge[1]) + ' ' + str(edge[2]) + '\n')
    file.close()
