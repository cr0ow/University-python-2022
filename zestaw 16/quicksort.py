def quicksort(L, left, right, comp):
    if comp(left, right) > -1:
        return
    swap(L, left, (left + right) // 2)
    pivot = left
    for i in range(left + 1, right + 1):
        if comp(L[left], L[i]) == 1:
            pivot += 1
            swap(L, pivot, i)
    swap(L, left, pivot)
    quicksort(L, left, pivot - 1, comp)
    quicksort(L, pivot + 1, right, comp)


def swap(L, left, right):
    L[left], L[right] = L[right], L[left]


# Funkcja porównująca zwraca
#  1  -  gdy pierwszy element jes większy od drugiego
#  0  -  gdy elementy są równe
# -1  -  gdy pierwszy element jest mniejszy od drugiego
# Szkielet takiej funkcji zamieszczam popniżej.
# Definicja 'większości', 'równości' i 'mniejszości'
# elementów zależy od implementacji warunków logicznych.
# W tym przypadku jest to proste porównanie dwóch liczb


def compare(left, right):
    if left > right:
        return 1
    if left == right:
        return 0
    if left < right:
        return -1
