#-----| PROGRAMANDO TABUADA DO 1 AO 10 COM 2 WHILES

tab =1 # Variável de 
while tab <= 10:
    print('Tabuada do {}'.format(tab))
    i = 1
   while i <= 10:
        print('{} X {} = {}'.format(tab, i, tab * i))
        i += 1
    tab+= 1