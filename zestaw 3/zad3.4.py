x = ''
while True:
	x = input("Podaj liczbe: ")
	if x == 'stop':
		break
	try:
		y = float(x)
	except ValueError:
		print("To nie jest liczba!")
		continue
	print('x = {x}'.format(x=y))
	print('x^3 = {x3}'.format(x3=y**3))
