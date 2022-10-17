def digits(num):
	a = 0
	while num > 0:
		num = int(num / 10)
		a += 1
	return a


result = ''
x = int(input("Długość miarki: "))
dots = digits(x) + 2
for i in range(x):
	result += '|'
	for j in range(dots):
		result += '.'

result += '|\n0'

for i in range(1, x + 1):
	b = digits(i)
	for j in range(dots - b + 1):
		result += ' '
	result += str(i)

print(result)
