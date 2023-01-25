from kruskal import kruskal
import graph as g
import convert as cv

filename = 'test1.txt'

print('Wczytanie grafu z pliku \'' + filename + '\'..\n')
graph, v = g.load_from_file(filename)

result = kruskal(graph)

print("Zapisanie wyniku do pliku 'result.txt'...\n")
g.save_to_file(result, "result.txt")

print('Graf wejściowy i wynik jako lista krawędzi:\n', graph, '\n', result, '\n')


graph = [[0, 7,  8,  3, 2, 0],
         [7, 0,  1,  0, 0, 0],
         [8, 1,  0, 12, 0, 4],
         [3, 0, 12,  0, 0, 6],
         [2, 0,  0,  0, 0, 5],
         [0, 0,  4,  6, 5, 0]]

result = kruskal(cv.matrix_to_edges(graph))
result = cv.edges_to_matrix(result)
print('Graf wejściowy i wynik jako macierz:\n', graph, '\n', result, '\n')

graph = [[(1, 7), (2, 8), (3, 3), (4, 2)],
         [(0, 7), (2, 1)],
         [(0, 8), (1, 1), (3, 12), (5, 4)],
         [(0, 3), (2, 12), (5, 6)],
         [(0, 2), (5, 5)],
         [(2, 4), (3, 6), (4, 5)]]

result = kruskal(cv.list_to_edges(graph))
result = cv.edges_to_list(result)
print('Graf wejściowy i wynik jako lista sąsiedztwa:\n', graph, '\n', result, '\n')
