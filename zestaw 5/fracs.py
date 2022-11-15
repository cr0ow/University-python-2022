import math


def add_frac(frac1, frac2):        # frac1 + frac2
	if frac1[1] == 0 or frac2[1] == 0:
		pass
	if frac1[1] == frac2[1]:
		return [frac1[0] + frac2[0], frac1[1]]
	nwd = math.gcd(frac1[1], frac2[1])
	nww = frac1[1] * frac2[1] / nwd
	x = nww / frac1[1]
	frac1[0] *= x
	frac1[1] = nww
	x = nww / frac2[1]
	frac2[0] *= x
	frac2[1] = nww
	return [frac1[0] + frac2[0], frac1[1]]


def sub_frac(frac1, frac2):        # frac1 - frac2
	if frac1[1] == 0 or frac2[1] == 0:
		pass
	if frac1[1] == frac2[1]:
		return [frac1[0] - frac2[0], frac1[1]]
	nwd = math.gcd(frac1[1], frac2[1])
	nww = frac1[1] * frac2[1] / nwd
	x = nww / frac1[1]
	frac1[0] *= x
	frac1[1] = nww
	x = nww / frac2[1]
	frac2[0] *= x
	frac2[1] = nww
	return [frac1[0] - frac2[0], frac1[1]]


def mul_frac(frac1, frac2):        # frac1 * frac2
	if frac1[1] == 0 or frac2[1] == 0:
		pass
	return [frac1[0] * frac2[0], frac1[1] * frac2[1]]


def div_frac(frac1, frac2):        # frac1 / frac2
	if frac1[1] == 0 or frac2[1] == 0:
		pass
	return [frac1[0] * frac2[1], frac1[1] * frac2[0]]


def is_positive(frac):             # bool, czy dodatni
	if frac[1] == 0:
		pass
	if frac[0] / frac[1] > 0:
		return True
	return False


def is_zero(frac):                 # bool, typu [0, x]
	if frac[1] == 0:
		pass
	if frac[0] == 0:
		return True
	return False


def cmp_frac(frac1, frac2):        # -1 | 0 | +1
	if frac1[1] == 0 or frac2[1] == 0:
		pass
	diff = frac2float(frac1) - frac2float(frac2)
	if diff > 0: return 1
	if diff == 0: return 0
	return -1


def frac2float(frac):              # konwersja do float
	if frac[1] == 0:
		pass
	return float(frac[0] / frac[1])
