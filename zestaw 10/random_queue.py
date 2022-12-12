from random import random


class RandomQueue:

    def __init__(self):
        self.items = []
        self.size = 0
        self.max_size = 5

    def insert(self, item):   # wstawia element w czasie O(1)
        if self.is_full():
            raise OverflowError("kolejka pełna")
        self.items.append(item)
        self.size += 1

    def remove(self):   # zwraca losowy element w czasie O(1)
        if self.is_empty():
            raise ValueError("kolejka pusta")
        idx = int(random() * self.size)
        item = self.items[idx]
        self.items[idx], self.items[self.size-1] = self.items[self.size-1], self.items[idx]
        self.items.pop()
        self.size -= 1
        return item

    def is_empty(self):
        return not self.items

    def is_full(self):
        return self.size == self.max_size

    def clear(self):   # czyszczenie listy
        self.items.clear()
