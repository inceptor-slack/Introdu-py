# Quantidade de kWh consumida
print('Qual é o tipo do seu imóvel')
print('Residêncial digite 1')
print('Industrial digite 2 ')
print('Comencial digite 3')
op = int(input())
if op == 1:
    kwh = float(input('Residência selecionada\n Qual o valor em kWh usados:'))
    if kwh > 500:
        calc = kwh * 0.65
        print('O total a pagar é {}'.format(calc))
    else:
        calc = kwh * 0.40
        print('O total a pagar é {}'.format(calc))
elif op == 2:
    kwh = float(input('Industrial selecionada\n Qual o valor em kWh usados:'))
    if kwh > 5000:
        calc = kwh * 0.60
        print('O total a pagar é {}'.format(calc))
    else:
        calc = kwh * 0.55
        print('O total a pagar é {}'.format(calc))
elif op == 3:
    kwh = float(input('Comercial selecionada\n Qual o valor em kWh usados:'))
    if kwh > 1000:
        calc = kwh * 0.60
        print('O total a pagar é {}'.format(calc))
    else:
        calc = kwh * 0.55
        print('O total a pagar é {}'.format(calc))
else:
    print('Opção inválida')


