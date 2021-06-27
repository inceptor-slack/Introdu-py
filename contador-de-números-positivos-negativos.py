while True:
    print(' ')
    inicio = int(input('Digite um numero inicial:'))# número que inicial da contagem
    final = int(input('Digite um numero final:'))# número final
#---------| Variáveis de controle
    qtd_negativo = 0
    qtd_positivo = 0
    qtd_par_positivo = 0
    qtd_impar_positivo = 0
    qtd_impar_negativo = 0
    qtd_par_negativos = 0
    cont = inicio
#----------| instrução
    if (inicio < final):#condição de controle para executar as intruções
        while (cont <= final):#controle de repetição será menor que a variável 'final'
            if (cont > 0):#condição de valor positivo ou negativo
                qtd_positivo += 1
                if (cont % 2 == 0):  # condição de valor par ou impar
                    qtd_par_positivo += 1
                else:
                    qtd_impar_positivo += 1
            else:
                qtd_negativo += 1
                if (cont % 2 == 0):#condição de valor par ou impar
                    qtd_par_negativos += 1
                else:
                    qtd_impar_negativo += 1
            cont += 1 #atribui +1 para repetição
        print('Quantidade de valores negativos {}'.format(qtd_negativo))
        print('Quantidade de valores positivos {}'.format(qtd_positivo))
        print('Quantidade de valores par {}'.format(qtd_par_positivo))
        print('Quantidade de valores impar {}'.format(qtd_impar_positivo))
        print('Quantidade de valores impar negativos {}'.format(qtd_impar_negativo))
        print('Quantidade de valores par positivos {}'.format(qtd_par_negativos))


    else:
        print('ERRRROu')
