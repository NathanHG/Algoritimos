altu = float(input('Digite um número para a altura: '))
base = float(input('Digite um número para a base: '))
while (altu <= 0 or base <= 0):
    altu = float(input('Dado inválido, digite a altura novamente: '))
    base = float(input('Dado inválido, digite a base novamente:'))
area = base * altu / 2
print('A área do triangulo é: {}'.format(area))
    
