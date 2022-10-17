import re

line = 'multiiii \n line \t \r\nabC GvR string'
word = 'word'
words = re.split('\\s+', line) # tablica słów w line
L = [12, 45, 73, 9, 150]

print("---2.10---")
print('liczba wyrazów w line: ', len(words))

print("\n---2.11---")
separated = ''
for letter in word:
	separated += letter + "_"
print('word oddzielone _ : ', separated.removesuffix("_"))

print("\n---2.12---")
first = ''
last = ''
for w in words:
	first += w[0]
	last += w[len(w) - 1]
print('słowo złożone z pierwszych liter słów w line: ', first)
print('słowo złożone z ostatnich liter słów w line: ', last)

print("\n---2.13---")
lens = []
for w in words:
	lens.append(len(w))
print('suma długości wszystkich słów w line: ',sum(lens))

print("\n---2.14---")
longest = ''
for w in words:
	if len(w) > len(longest):
		longest = w
print('najdłuższe słowo: ', longest)
print('długość najdłużeszego słowa: ', len(longest))

print("\n---2.15---")
as_string = ''
for i in L:
	as_string += str(i)
print(as_string)

print("\n---2.16---")
print(line.replace("GvR", 'Guido van Rossum'))

print("\n---2.17---")
print('posortowane alfabetycznie: ', sorted(words, key=str.lower))
print('posortowane po długości: ', sorted(words, key=len))

print("\n---2.18---")
as_string = str(10324230042)
num_of_zeros = 0
for i in as_string:
	if i == '0':
		num_of_zeros+=1
print('ilość zer w liczbie {0}: {1}'.format(as_string, num_of_zeros))

print("\n---2.19---")
filled = []
for i in L:
	filled.append(str(i).zfill(3))
print(filled)
