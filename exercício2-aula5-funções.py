while True:
    palavra = input('digite algo:')
    nome = 'henrique'
    def valido():
        res= palavra >= nome
        return res

    retorno = valido()
    print(retorno)