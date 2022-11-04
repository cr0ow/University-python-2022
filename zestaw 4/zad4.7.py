def flat_one_item(item, _res):
	for i in item:
		if isinstance(i, (list, tuple)):
			return flat_one_item(i, _res)
		_res.append(i)
	return _res


def flatten(sequence):
	result = []
	for item in sequence:
		if isinstance(item, (list, tuple)):
			temp = flat_one_item(item, [])
			for t in temp:
				result.append(t)
		else:
			result.append(item)
	return result


L = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(flatten(L))
