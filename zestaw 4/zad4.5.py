def odwracanie(L, left, right):
	j = right
	i = left
	while i < j:
		L[i], L[j] = L[j], L[i]
		i = i + 1
		j = j - 1
	return L


def odwracanie_rek(L, left, right):
	L[left], L[right] = L[right], L[left]
	if left == right or left + 1 == right:
		return L
	return odwracanie_rek(L, left + 1, right - 1)


L1 = [1, 2, 3, 4, 5, 6, 7, 8]
L2 = [1, 2, 3, 4, 5, 6, 7, 8]
l = int(input('Podaj left: '))
r = int(input('Podaj right: '))
print(odwracanie(L1, l, r))
print(odwracanie_rek(L2, l, r))
