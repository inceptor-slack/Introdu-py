# --------| ROTINA |-------

def valida_texto(pergunta, min, max):# função para validar o tamanho do texto
    s1 = input(pergunta)# inserção da do texto para variável 's1'
    tam = len(s1)# contando a quantidade de caractéres no texto
    while ((tam < min) or (tam > max)):# condição de controle do tamanho
        s1 = input(pergunta)# se a condição não for satisfeita 
        tam = len(s1)# repete a pergunta e mede-se o tamanho do texto
    return s1
# ------|PROGRAMA PRINCIPAL |-------
x = valida_string('Digite uma string: ', 10, 30)# variável 'x' recebe a função de validação
print('Você digitou o texto: {}. \nValor válido.'.format(x))# se as condições forem satisfeitas imprime na tela o texto