# Algorytm Kruskala

### Autor: Marcin Wrona

\
Jako projekt zaliczeniowy wybrałem algorytm Kruskala. Jest to algorytm grafowy
wyznaczający minimalne drzewo rozpinające dla grafu nieskierowanego ważonego,
o ile jest on spójny.


Algorytm znajaduje się w pliku `kruskal.py` i wymaga podania grafu w postaci listy krawędzi:

`````
[(wierzchołek1, wierzchołek2, waga_krawędzi), (wierzchołek1, wierzchołek2, waga_krawędzi)...]
`````

W pliku `convert.py` znajdują się konwertery, które pozwalają zmienić postać grafu. Dzięki 
nim można zamienić reprezentację grafu z macierzy sąsiedztwa na listę krawędzi i odwrotnie, 
oraz z listy sąsiedztwa na listę krawędzi i odwrotnie.

Plik `graph.py` zawiera funkcje do odczytu i zapisu grafu do pliku. Plik, z którego funkcja 
odczytuje graf musi mieć postać:

````
liczba_wierzchołków
liczba_krawędzi
wierzchołek1 wierzchołek2 waga
wierzchołek1 wierzchołek2 waga
...
````

Przykładowy graf można znaleźć w pliku `test1.txt`.

### Zawartość plików

Plik `kruskal.py` zawiera:

##### Klasy: 
 - `Node` - reprezentuje ona wierzchołek w grafie, pomocny dla funkcji `union()`, zawiera pola:
   - `value` - wartość wierzchołka
   - `rank` - reprezentuje wysokość poddrzewa wierzchołka
   - `parent` - wskazuje na rodzica wierzchołka

##### Funkcje:
 - `find(x)` - znajduje najdalszego rodzica wierzchołka, przyjmuje obiekt klasy `Node`
 - `union(x, y)` - złącza poddrzewa wierzchołków x i y w jedno  wspólnym rodzicu, przyjmuje dwa obiekty klasy Node
 - `kruskal(edges)` - właściwy algorytm, argumentem jest graf w postaci listy krawędzi:
   - `vertices` - lista wierzchołków w grafie
   - `MST` - graf wynikowy (przedstawiony za pomocą listy krawędzi)
   - `V` - lista wierzchołków grafu wynikowego na których przeprowadzane są dalsze operacje
 
Plik `convert.py` zawiera:

##### Funkcje:
 - `matrix_to_edges(_matrix)` - konwertuje graf z postaci macierzowej do postaci listy krawędzi
 - `edges_to_matrix(_edges)` - konwertuje graf z postaci listy krawędzi do postaci macierzowej
 - `list_to_edges(_list)` - konwertuje graf z postaci listy sąsiedztwa do postaci listy krawędzi
 - `edges_to_list(_list)` - konwertuje graf z postaci listy krawędzi do postaci listy sąsiedztwa
 - `read_vertices(_edges)` - zwraca listę wierzchołków w grafie o postaci listy krawędzi

Plik `graph.py` zawiera:

##### Funkcje:
 - `load_from_file(filename)` - wczytuje graf z pliku o podanej nazwie
 - `save_to_file(graph, filename)` - zapisuje graf o postaci listy krawędzi do pliku o podanej nazwie

Plik `main.py` zawiera test wszystkich funkcjonalności z wyżej wymienionych plików.
