print("Exercício 03")
N = []
n = 1
s = 0
while (n >= 0):
    N.append(n)
    n = int(input("Digite a nota: "))
    s = s + n 
del N[0]
print(N)
print(s + 1)
