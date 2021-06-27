print('Calculadora')
num1 = float(input('Digite um valor:'))
op = input('Um operador:')
num2 = float(input('Outro valor:'))

while True:

    if(op == '+'):
        res = num1 + num2
        print(res)
    elif(op == '-'):
        res = num1 - num2
        print(res)
    elif(op == '*'):
        res = num1 * num2
        print(res)
    elif (op == '/'):
        res = num1 / num2
        print(res)
    elif(op == 's'):
        break
    else:
        print('Operação Inválida')

    num1 = float(input('Digite um valor:'))
    op = input('Um operador:')
    num2 = float(input('Outro valor:'))

