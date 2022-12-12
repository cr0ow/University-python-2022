from single_list import SingleList
from node import Node

alist = SingleList()
alist.insert_head(Node(11))   # [11]
alist.insert_head(Node(22))   # [22, 11]
alist.insert_tail(Node(33))   # [22, 11, 33]
print("length {}".format(alist.length))   # odczyt atrybutu
print("length {}".format(alist.count()))   # wykorzystujemy interfejs

blist = SingleList()
blist.insert_head(Node(11))   # [11]
blist.insert_head(Node(22))   # [22, 11]
blist.insert_tail(Node(33))   # [22, 11, 33]
blist.insert_tail(Node(44))   # [22, 11, 33, 44]
print("length {}".format(blist.length))   # odczyt atrybutu
print("length {}".format(blist.count()))   # wykorzystujemy interfejs

alist.clear()

while not alist.is_empty():   # kolejność 22, 11, 33
    print("remove tail {}".format(alist.remove_tail()))

while not blist.is_empty():   # kolejność 22, 11, 33
    print("remove tail {}".format(blist.remove_tail()))


