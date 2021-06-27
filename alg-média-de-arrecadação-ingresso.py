#---------| Média de arrecadação do cinema |--------
#----| Proposta do exercício criar um algoritmo que conte o total de pessoas
# e arrecadção de ingresso no cinema, com os seguintes parâmetros, menor de 3 anos não paga,
# maior de 13 anos paga inteira de 30R$ e entre 3 e 12 paga metade
total = 0
grana = 0
while True:#laço
    idade = input('Digite sua idade:')# entrada da variável que será string
    if idade == 'sair':# se escrever 'sair' o algortimo para
        break
    idade = int(idade)# conversão de string para número inteiro
    total += 1# 'total recebe +1
    if idade < 3:
        ingresso = 0
    else:
        if idade > 13:
            ingresso = 30
        else:
            ingresso = 15

    grana += ingresso
media = grana / total
print('Total de pessoas {}'.format(total))
print('Total de arrecadado {}R$'.format(grana))
print('Média de arrecadada por pessoa {}R$'.format(media))