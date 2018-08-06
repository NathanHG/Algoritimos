print('***** Ex. 6 *****')
contagem = 0
num_fibonacci_1 = 0
num_fibonacci_2 = 1
termo = 2
print('A sequencia de fibonacci é: \n{}º termo: {} \n{}º termo: {}'.format(1, num_fibonacci_1, 2, num_fibonacci_2))
for contagem in range (1, 9, 3):
      termo = termo + 1
      num_fibonacci_1 = num_fibonacci_1 + num_fibonacci_2
      print('{}º termo: {}'.format(termo, num_fibonacci_1))
      termo = termo + 1
      num_fibonacci_2 = num_fibonacci_1 + num_fibonacci_2
      print('{}º termo: {}'.format(termo, num_fibonacci_2))
      
