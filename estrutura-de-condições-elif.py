#------------| ESTRUTURA DE CONDIÇÃO ELIF |---------
print('Escolha a fruta de deseja:')
print('1 = Banana')
print('2 = Maça')
print('3 = Laranja')

produto = int(input('Qual fruta vai querer? '))

qtd = int(input('Qual a quantidade '))

if(produto == 1):
    pagar = qtd * 1.85
    print('Você comprou {} {} e custa {}R$'.format(qtd,produto,pagar))

elif(produto == 2):
        pagar = qtd *2.30
        print('Você comprou {} {} e custa {}R$'.format(qtd,produto,pagar))

elif(produto == 3):
        pagar = qtd *3.60
        print('Você comprou {} {} e custa {}R$'.format(qtd,produto,pagar))

else:
    print('Produto inexistente')