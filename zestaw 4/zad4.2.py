def digits(num):
	a = 0
	while num > 0:
		num = int(num / 10)
		a += 1
	return a


def make_ruler(length):
	result = ''
	dots = digits(length) + 2
	for i in range(length):
		result += '|'
		for j in range(dots):
			result += '.'
	result += '|\n0'
	for i in range(1, length + 1):
		b = digits(i)
		for j in range(dots - b + 1):
			result += ' '
		result += str(i)
	return result


def make_grid(x, y):
	part1 = ''
	for i in range(x):
		part1 += '+---'
	part1 += '+\n'

	part2 = ''
	for i in range(x):
		part2 += '|   '
	part2 += '|\n'

	result = ''
	for i in range(y):
		result += part1 + part2
	result += part1
	return result


print(make_ruler(int(input("Długość miarki: "))))
x = int(input('Podaj szerokość: '))
y = int(input('Podaj wysokość: '))
print(make_grid(x, y))
