class Stack:

    def __init__(self):
        self.items = []
        self.size = 0
        self.max_size = 5

    def __str__(self):                  # podglądamy stos
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):                  # nigdy nie jest pełny
        return self.size == self.max_size

    def push(self, item):
        if self.is_full():
            raise ValueError("stos pełny")
        self.size += 1
        self.items.append(item)         # dodajemy na koniec

    def pop(self):                      # zwraca element
        if self.is_empty():
            raise ValueError("stos pusty")
        self.size -= 1
        return self.items.pop()         # zabieram od końca