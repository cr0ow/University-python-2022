def fibonacci(n):
	if n == 0 or n == 1:
		return n
	f1, f2, result = 1, 1, 0
	for i in range(3, n+1):
		result = f1 + f2
		f1, f2 = f2, result
	return result


print(fibonacci(int(input('Podaj liczbe nieujemną: '))))
