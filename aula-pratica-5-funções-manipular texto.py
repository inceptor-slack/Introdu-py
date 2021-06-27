# ---------|     EXERCÍCIO 2
# Proposta:
# suponha que você é um colecionador de jogos de videogame. Escreva um algoritmo que
# permina cadastrar esses jogos informando o nome e a qual videogame ele pertence.
# Para isso, crie um menu de opções contendo: cadastrar novo item, listar o que
# foi cadastrado e sair.
# Para resolve o exercício crie pelo menos uma função para cada item do menu
# Além disso, armazene todos os dados em um arquivo de texto que deve ser salvo em disco
# e manter os dados cadastrados.

# -------| ROTINAS DO PROGRAMA |---------

def valida_int(pergunta,min,max):# função para validar a escolha do usuário
    x = int(input(pergunta))
    while((x<min) or (x>max)):
        x = int(input(pergunta))
    return x

def criaArquivo(nomearquivo):# cria um arquivo de texto caso ele não exista
    try:
        a = open(nomearquivo,'wt+')
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso')

def existeArquivo(nomearquivo):# verifica se o arquivo existe
    try:
        a = open(nomearquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def cadastrarJogo(nomearquivo, nomeJogo, nomeVideogame):# função para adicionar o jogo ao arquivo de texto
    try:
        a = open(nomearquivo, 'at')
    except:
        print('Erro ao abrir arquivo')
    else:
        a.write('{};{}\n'.format(nomeJogo,nomeVideogame))
    finally:
        a.close()
def listarArquivo(nomearquivo):# lista todos os dados já escrito no arquivo de texto
    try:
        a = open(nomearquivo, 'rt')
    except:
        print('Erro ao abrir arquivo')
    else:
        print(a.read())
    finally:
        a.close()



# ----|PROGRAMA PRINCIPAL

arquivo = 'games.txt' # variável global do arquivo de texto
if existeArquivo(arquivo):# condição para verificar se o arquivo existe
    print('Arquivo localizado')
else:
    print('O Arquivo não existe')
    criaArquivo(arquivo)
while True:# laço principal para os cadastros e listagem
    print('Menu')
    print('1-Cadastrar um novo item')
    print('2-Listar item cadastrados')
    print('3-Sair')
    op = valida_int('Escolha sua opção:',1,3)
# -------| CONDIÇÕES DE OPERAÇÃO |------
    if op == 1:
        print('Opção 1 selecionada\n')
        nomeJogo = input('Nome do game:')
        nomeVideogame = input('Nomo do Videogame:')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

    elif op == 2:
        print('Opção 2 selecionada\n')
        listarArquivo(arquivo)

    elif op == 3:
        print('Opção 3 selecionada\n')
        break

# ------------| ALGUMAS FUNÇÕES PARA MANIPULAR ARQUIVOS |--------
# ----| MODO |-----| OPERAÇÃO
# ----|   r  |-----| leitura
# ----|   w  |-----| escrita, apaga o conteúdo se já existir
# ----|   a  |-----| escrita, mas preserva o conteúdo se já existir
# ----|   b  |-----| modo binário
# ----|   +  |-----| atualização (leitura e escrita)
# ----|   t  |-----| para saber se o arquivo é txt
# fechar arquivos: arquivo.close()
# ler arquivo: arquivo.read(), arquivo.readlines()
# escrever arquivo: arquivo.write()
