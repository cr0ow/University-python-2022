x = int(input('Podaj szerokość: '))
y = int(input('Podaj wysokość: '))

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

print(result)
