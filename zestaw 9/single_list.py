class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):   # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self):  # klasy O(n)
        if not self.head:
            raise ValueError("lista pusta")
        i = self.head
        if self.head == self.tail:
            self.clear()
            self.length -= 1
            return i
        while i.next is not self.tail:
            i = i.next
        node = i.next
        i.next = None
        self.tail = i
        self.length -= 1
        return node

    def join(self, other):   # klasy O(1)
        self.tail.next = other.head
        self.tail = other.tail
        other.clear()

    def clear(self):   # czyszczenie listy
        self.head = self.tail = None
