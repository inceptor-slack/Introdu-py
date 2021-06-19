print('Qual é a forma de pagamento:')
print(' 1. Pagamento à vista.')
print(' 2. Parcelamento à prazo.')

op = int(input('Digite a opção:')) #entra a escolha da operação
#---------------|   PAGAMENTO À VISTA    |------------------
if op == 1:
    print('Pagamento à Vita Selecionado')
    valor = float(input('Digite o valor a pagar:'))
    desc = float(input('Digite a porcentagem de desconto:'))
    valor_final = (valor / 100) * desc
    pag = valor - valor_final
    print('O total a pagar é de {:.2f}R$, com desconto de {:.2f}R$'.format(pag, valor_final))
#---------------|   PARCELAMENTO |------------------
elif op == 2:
    print('Parcelamento à Prazo Selecionado.')
    valor = float(input('Digite o valor a pagar:'))
    parcela = int(input('Digite a quantidade de parcelas')
    juros = float(input('Digite a porcentagem de juros'))
    valor_final = valor / parcela
    print('Às parcelas seram {} de {:.2f}R$ mensais'.format(parcela, valor_final))