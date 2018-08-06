nota = float(input('Notas: '))
s_n = 0
qnt = 0
while (nota >= 0):
    s_n = s_n + nota
    qnt = qnt + 1
    nota = float(input('Notas: '))
media = (s_n / qnt)
print('A média de notas foi: {}'.format(media))
