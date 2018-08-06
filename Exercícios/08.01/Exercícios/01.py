print("Exercício 01")
M = 0
m = 0
s = 0
i = 0
M18 = 0
x = 0
L = [8,0,97,105,21,303]
for x in L:
    if x >= M:
        M = x
print("O maior número é {}.".format(M))
for x in L:
    if x <= m:
        m = x
print("O menor número é {}.".format(m))
for x in L:
    s = s + x
print("A soma  dos elementos de L é {}.".format(s))
print("Números ímpares: ")
for x in L:
    if (x % 2 != 0):
        print(x)
print("Números maiores do que 18: ")
for x in L:
    if (x  > 18):
        print(x)
