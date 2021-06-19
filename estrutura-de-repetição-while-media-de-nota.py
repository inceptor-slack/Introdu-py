#--------| WHILE PARA MÉDIA DE NOTA |---------
soma = 0 # Variável para receber o valor da nota
cont = 1 # Variável para contar os loops
while (cont <= 5): # Laço de repetição
    nota = float(input('Digite a {}ª nota:'.format(cont))) # Entrada da nota
    soma = soma + nota # Atribuição de soma com a nota
    cont = cont + 1 # Para cada intrução a variável 'cont' reberá + 1 ate completar o valor de 5
media = soma / 5 # calculo da média, repare que ele esta paralelo ao while  e será executado depois de 5 loops
print('Média final: {}' .format(media))# Imprimi na tela a nota