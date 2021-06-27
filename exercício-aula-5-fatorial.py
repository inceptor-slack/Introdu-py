# -----| FATORIAL ALG
def valida_int(pergunta,min,max):
    """
    Valídação para saber se o valor da variável é inteiro
    :param pergunta: para inserir um valor
    :param min: é um valor fixo de 0, que é o limite mínimo
    :param max: também um valor fixo para o maxímo
    :return:
    """
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x
def fatorial(num):
    fat = 1
    if num == 0:
        return  fat
    for i in range(1,num+1,1):
        fat *= i
    return fat

x = valida_int('Insira um valor:',0,999999)
print('{}! = {}'.format(x,fatorial(x)))
