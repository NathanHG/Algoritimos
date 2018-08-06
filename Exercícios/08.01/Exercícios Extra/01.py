print("Exercício Extra 01")
n = 0
x = 0
m = 0
for x in range (1, 6, 1):
    n = int(input("Digite um número: "))
    if (n >= m):
        m = n
print("O maior número é {}.".format(m))
