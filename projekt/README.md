# Algorytm Kruskala

### Autor: Marcin Wrona

\
Jako projekt zaliczeniowy wybrałem algorytm Kruskala. Jest to algorytm grafowy \
wyznaczający minimalne drzewo rozpinające dla grafu nieskierowanego ważonego, \
o ile jest on spójny. \
\
Przygotowałem dwie wersje algorytmu, tak aby możliwe było przekazanie grafu w postaci:
 - macierzy sąsiedztwa (plik Algorytm-Kruskala-macierz.py)
 - listy sąsiedztwa (plik Algorytm-Kruskala-lista.py)

### Reprezentacja grafu macierzą sąsiedztwa 
Plik Algorytm-Kruskala-macierz.py zawiera: \
\
Klasy: 
 - Node - reprezentuje ona wierzchołek w grafie wynikowym, zawiera pola:
   - value - wartość wierzchołka
   - rank - reprezentuje wysokość poddrzewa wierzchołka
   - parent - wskazuje na rodzica wierzchołka

Funkcje:
 - find(x) - znajduje najdalszego rodzica wierzchołka, przyj,uje obiekt klasy Node
 - union(x, y) - złącza poddrzewa wierzchołków x i y w jedno  wspólnym rodzicu, przyjmuje dwa obiekty klasy Node
 - make_set(v) - tworzy obiekt klasy Node, na których są wykonywane dalsze operacje, przyjmuje wartoć wierzchołka
 - convert_to_edges(graph) - zwraca listę wszystkich krawędzi grafu, przyjmuje graf w postaci macierzy sąsiedztwa
 - kruskal(graph) - właściwy algorytm, argumentem jest graf w postaci macierzy sąsiedztwa, oznaczenia zmiennych:
   - edges - lista zawierająca krawędzie grafu wejściowego
   - MST - graf wynikowy (przedstawiony za pomocą listy krawędzi)
   - V - lista wierzchołków grafu wynikowego na których przeprowadzane są dalsze operacje


### Reprezentacja grafu listą sąsiedztwa 
Plik Algorytm-Kruskala-lista.py zawiera: \
\
Klasy: 
 - Node - reprezentuje ona wierzchołek w grafie wynikowym, zawiera
   - value - wartość wierzchołka
   - rank - reprezentuje wysokość poddrzewa wierzchołka
   - parent - wskazuje na rodzica wierzchołka

Funkcje:
 - find(x) - znajduje najdalszego rodzica wierzchołka, przyj,uje obiekt klasy Node
 - union(x, y) - złącza poddrzewa wierzchołków x i y w jedno  wspólnym rodzicu, przyjmuje dwa obiekty klasy Node
 - make_set(v) - tworzy obiekt klasy Node, na których są wykonywane dalsze operacje, przyjmuje wartoć wierzchołka
 - convert_to_edges(graph) - zwraca listę wszystkich krawędzi grafu, przyjmuje graf w postaci listy sąsiedztwa
 - kruskal(graph) - właściwy algorytm, argumentem jest graf w postaci listy sąsiedztwa, oznaczenia zmiennych:
   - edges - lista zawierająca krawędzie grafu wejściowego
   - MST - graf wynikowy (przedstawiony za pomocą listy krawędzi)
   - V - lista wierzchołków grafu wynikowego na których przeprowadzane są dalsze operacje
