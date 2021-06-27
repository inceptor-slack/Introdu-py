# Proposta do exercício
# Escreva uma  rotina uma borda ao redor de uma palavra para destacá-la
# como sendo um título. A rotina deve receber como parâmetro a palavra
# a ser destacada. O tamanho da caixa de texto de ser adptável de acordo
# com o tamanho da palavra.
while True:
    print(' ')
    palavra = input('Escreva algo:')
    print(' ')
    tam = len(palavra)
    def teste1():
        print('+','-' * tam,'+')
        print('|',palavra,'|')
        print('+', '-' * tam,'+')
    teste1()