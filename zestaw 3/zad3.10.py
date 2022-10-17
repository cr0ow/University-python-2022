roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
         'C': 100, 'D': 500, "M": 1000}


def roman2int(num):
	tab = []
	for i in num:
		tab.append(i)
	result = 0
	for i in range(len(tab) - 1):
		if roman[tab[i]] < roman[tab[i + 1]]:
			result -= roman[tab[i]]
		else:
			result += roman[tab[i]]
	result += roman[tab[len(tab) - 1]]
	return result


print(roman2int('MCDLVI'))
