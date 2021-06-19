#-----|programando tabuada com 2 for

tab = 1

for tab in range(1,11,1):
    print('TABUADA DO {}'.format(tab))
    i = 1
    for i in range(1,11,1):
        print('{} X {} = {}'.format(tab, i, tab * i))