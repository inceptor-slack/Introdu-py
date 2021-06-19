print('CALCULATION 3000')
#-----------| ENTADA DAS VARIÁVEIS |-----------
n1 = float(input())#--PRIMEIRO NÚMERO
op = input()#---OPERADOR ESCOLHIDO
n2 = float(input())#--SEGUNDO NÚMERO

#-------| CONDICIONAIS DE MÚLTILA ESCOLA USANDO (ELIF)|-----
if op == '+':
    res = n1 + n2
    print(res)
elif op == '-':
    res = n1 -n2
    print(res)
elif op == '/':
    res = n1 / n2
    print(res)
elif op == '*':
    res = n1 * n2
    print(res)
else:
    print('sintaxe error')