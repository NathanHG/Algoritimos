# Faça um programa para mostrar as tabuadas dos números de 1 a 10.
print('~~~~~ Ex. 5  ~~~~~')
multiplicador = 1 
multiplicando = 1
resultado = 1
for multiplicador in range (0, 10):
      multiplicador = multiplicador + 1
      for multiplicando in range (1, 11):
            resultado = multiplicador * multiplicando
            print('tabuada de {}, é {} x {} = {}'.format(multiplicador, multiplicador, multiplicando, resultado))    

