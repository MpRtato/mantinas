nosaukums= 'masveidapardevetajs' +'.exe'

import os
import time

dir= os.getcwd()
dirl=os.listdir(dir)

if nosaukums in dirl:
    fskaits = str(len(dirl)-1)

else:
    fskaits=str(len(dirl))


print('Vai velaties pardevet {} failus no '.format(fskaits)+'['+dir+']'+'?(ja/ne)')

i=0
for j in dirl:
    fails = os.path.join(dir, dirl[i])

    if os.path.isfile(fails)==False:
        print('# '+dirl[i]+' /mape/')

    elif dirl[i]!= nosaukums:
        print('# '+dirl[i])

    i=i+1

while 1<2:
    jane=input('>')
    print(jane)
    if jane == 'ja' or jane =='Ja' or jane =='jA' or jane =='JA':
        break

    elif jane == 'ne' or jane == 'Ne' or jane == 'nE' or jane == 'NE':
        os._exit(1)

    else:
        print('Nepareiza ievade!')

print('')
print('Ievadiet pardevesanas nosaukumu: ')

#nosaukuma ievade
stop=0
while stop!=1:
    atb=input('>')
    atb=str(atb)

    simboli=['/','\\', ':', '*', '?', '"','<','>','|']
    i=0
    jep=0
    for j in simboli:
        if simboli[i] in atb:
            print('')
            print('Nosaukums neatbilst LOGA standartiem!')
            jep=1
            break

        elif i==len(simboli)-1 and jep==0:
            stop=1
            break

        i=i+1

#pardevesana
print('')
print('Faili tiek pardeveti:')
fail=0
mape=0
nr=1
i=0
for j in dirl:
    old=dirl[i]
    oldf=old.split('.')
    old=os.path.join(dir, dirl[i])
    if nosaukums in dirl[i]:
        time.sleep(0)

    else:
        if os.path.isfile(old)==False:
            mape=1
            nosauk = atb + '{}'.format(nr)

        else:
            if len(oldf)==1:
                nosauk = atb + '{}'.format(nr)

            else:
                nosauk=atb+'{}'.format(nr)+'.'+oldf[-1]

        new = os.path.join (dir, nosauk)

        dirljaun = os.listdir(dir)
        if nosauk in dirljaun:
            print('')
            print('Jau pastav fails ar tadu nosaukumu!')
            fail=1
            break

        os.rename(old, new)
        if mape==1:
            print('{}) '.format(nr)+nosauk+' /mape/')

        else:
            print('{}) '.format(nr)+nosauk)

        nr=nr+1

    mape=0
    i=i+1

if fail!=1:
    print('')
    print('')
    print('{} faili veiksmigi pardeveti par '.format(fskaits)+'"'+atb+'"')
    time.sleep(3)

else:
    os._exit(1)