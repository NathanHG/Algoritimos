print("Exercício Extra 06")
n = int(input("Digite um número: "))
i = int(input("Digite outro número: "))
j = int(input("Digite mais um outro número: "))
x = 0
cont = 0
while (cont <= n - 1 ):
    if (x % i == 0 or x % j == 0):
        cont  = cont + 1
        print(x)
    x = x + 1
