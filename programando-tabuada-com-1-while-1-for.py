#-----|programando tabuada com while + for

tab = 1

while tab <= 10:
    print('TABUADA {}'.format(tab))
    for i in range (1,11,1):
        print('{} X {} = {}'.format(tab, i, tab * i))
    tab += 1