print("---3.1---")
# kod poprawny:
# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;

# kod niepoprawny:
# for i in "axby": if ord(i) < 100: print(i)
# ponieważ nie są zachowane odpowiednie wcięcia w kodzie

# kod poprawny:
# for i in "axby": print (ord(i) if ord(i) < 100 else i)

print("---3.2---")
# L = [3, 5, 4] ; L = L.sort()  # OK
# x, y = 1, 2, 3                # 3 nie zostanie przypisane do żadnej zmiennej
# X = 1, 2, 3 ; X[1] = 4        # zmienna X nie jest litą
# X = [1, 2, 3] ; X[3] = 4      # X nie ma elementu o indeksie 3
# X = "abc" ; X.append("d")     # string nie ma metody append()
# L = list(map(pow, range(8)))  # OK

print("---3.3---")
result = ''
for i in range(30):
    if i % 3 != 0:
        result += str(i) + ', '
print(result)
