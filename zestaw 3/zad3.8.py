l1 = 'sgfsgr456tjnr'
l2 = 'dffopgdi3454a'

# (a)
result_a = []
for i in l1:
	for j in l2:
		if i == j and i not in result_a:
			result_a.append(i)
print('a) ', result_a)

# (b)
result_b = []
for i in l1:
	if i not in result_b:
		result_b.append(i)
for i in l2:
	if i not in result_b:
		result_b.append(i)
print('b) ', result_b)
