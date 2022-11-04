def sum_one_item(item, _sum):
	for i in item:
		if isinstance(i, (list, tuple)):
			return sum_one_item(i, _sum)
		_sum += i
	return _sum


def sum_seq(sequence):
	result = 0
	for item in sequence:
		if isinstance(item, (list, tuple)):
			result += sum_one_item(item, 0)
		else:
			result += item
	return result


L = [1, 2, [3, 4], 6, [5, [6, 7]]]
print(sum_seq(L))
