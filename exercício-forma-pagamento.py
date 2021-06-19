print('Qual é a forma de pagamento:')
print(' 1. Pagamento à vista.')
print(' 2. Parcelamento em 3x.')
print(' 3. Parcelamento em 5x.')
print(' 4. Parcelamento em 10x.')
op = int(input('Digite a opção:')) #entra a escolha da operação
#---------------|   PAGAMENTO À VISTA    |------------------
if op == 1:
    print('Pagamento à vita selecionado')
    valor = float(input('Digite o valor a pagar:'))
    desc = float(input('Digite a porcentagem de desconto:'))
    valor_final = (valor / 100) * desc
    pag = valor - valor_final
    print('O total a pagar é de {:.2f}R$, com desconto de {:.2f}R$'.format(pag, valor_final))
#---------------|   PARCELAMENTO EM 3X   |------------------
elif op == 2:
    print('Parcelamento em 3x selecionado.')
    valor = float(input('Digite o valor a pagar:'))
    valor_final = valor / 3
    print('Às parcelas seram 3 de {:.2f}R$ mensais'.format(valor_final))
#---------------|   PARCELAMENTO EM 5X   |------------------
elif op == 3:
    print('Parcelamento em 5x selecionado')
    valor = float(input('Digite o valor a pagar:'))
    juros = float(input('Digite a porcentagem de juros:'))
    valor_final = (valor / 100) * juros
    pag = valor_final + valor
    print('Às parcelas será 5x de {:.2f}R$ mensais, com juros embutido de {}% no total a prazo.'.format(pag, juros))
#---------------|   PARCELAMENTO EM 10X  |------------------
elif op == 4:
    print('Parcelamento em 10x selecionado')
    valor = float(input('Digite o valor a pagar:'))
    juros = float(input('Digite a porcentagem de juros:'))
    valor_final = (valor / 100) * juros
    pag = valor_final + valor
    print('Às parcelas será 10x de {:.2f}R$ mensais, com juros embutido de {}% no total a prazo.'.format(pag, juros))
#---------------|   OPÇÃO INVÁLIDA       |------------------
else:
    print('OPÇÃO INVÁLIDA')
