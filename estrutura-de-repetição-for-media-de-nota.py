#-------| FOR PARA MÉDIA DE NOTA |------

#-------| declaração das variáveis |---
soma = 0
cont = 1
#-----| função For para calcular a média |-----
for cont in range(1,6,1):# o "range" é uma função de intervalo já os três números dentro dos parenteses, o primeiro indica o valor inicial do iterador, o segundo valor final do iterador e o terceiro o passo do interador que no caso será de 1 em 1
    nota = float(input(('Digite a {}ª nota:'.format(cont))))
    soma = soma + nota
    cont = cont + 1
media = soma / 5
print('A média final é de {}'.format(media))