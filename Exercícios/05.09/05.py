a = int(input('Digite o número de um lado do triângulo: '))
b = int(input('Digite o número de outro lado do triângulo: '))
c = int(input('Digite um número pra um ultimo dos lado do triângulo: '))
if a<b+c and b<a+c and c<a+b:
    print('Isso é um triângulo.')
    if a==b and b==c :
        print('Esse triangulo é equilátero.')
    elif a==b and b!=c  :
        print('Esse triângulo é isósceles.')
    else:
        print('Esse triângulo é escaleno.')
else:
    print('Isso não é um triângulo')
