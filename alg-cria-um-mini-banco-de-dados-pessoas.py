# ----| Proposta do algoritimo |------
# Criar um mini banco de dados, onde será adicionado nome, idade, gênero
# e data de nascimento
# -----------------| ROTINAS |-------------------
def valida_op(pergunta,min,max):
    x = int(input(pergunta))
    while((x<min)or(x>max)):
        x = int(input(pergunta))
    return x
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
    except:
        print('ERRO NA CRIAÇÃO DO ARQUIVO')
    else:
        print('ARQUIVO CRIADO COM SUCESSO')
def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('ERRO AO ABRIR ARQUIVO')
    else:
        print(a.read())
    finally:
        a.close()
def cadastroUsuario(nomeArquivo,nomeUsuario,idade,genero,data_nasc):
    try:
        a = open(nomeArquivo,'at')
    except:
        print('ERRO AO ABRIR O ARQUIVO')
    else:
        a.write('{} ; {} ; {} ; {}\n'.format(nomeUsuario,idade,genero,data_nasc))
    finally:
        a.close()
# -------------|PROGRAMA PRINCIPAL|--------------
arquivo = 'estudo-dados.txt'
if existeArquivo(arquivo):
    print('Arquivo Localizado')
else:
    print('O Arquivo não Existe')
    criaArquivo(arquivo)
while True:
    print('--| MENU |--')
    print('1 - Cadastrar um usuário: ')
    print('2 - Listar usuário cadastrados: ')
    print('3 - Sair: ')
    op = valida_op('Escolha uma opção:', 1, 3)
# --------| CONDIÇÕES DA OPERAÇÃO |-------------
    if op == 1:
        print('Cadastrar um Usuário selecionado.')
        nomeUsuario = input('Digite o nome completo:')
        nomeUsuario = nomeUsuario.upper()
        idade = input('Digite a idade:')
        genero = input('Qual seu gênero:')
        genero = genero.upper()
        data_nasc = input('Digite sua data de nascimento:',)
        cadastroUsuario(arquivo,nomeUsuario,idade,genero,data_nasc)
    elif op == 2:
        print('Listar Dados selecionado.\n')
        listarArquivo(arquivo)
    elif op == 3:
        print('Programa Encerrado\n')
        break