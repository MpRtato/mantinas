import os
import time

dir= os.getcwd()
dirl=os.listdir(dir)

print('Vai velaties pardevet sos failus?(ja/ne)')

i=0
for j in dirl:
    print(dirl[i])
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
i=0
for j in dirl:
    old=dirl[i]
    oldf=old.split('.')
    old=os.path.join(dir, dirl[i])
    if 'masveidapardevetajs.exe' in dirl[i]:
        time.sleep(0)

    else:

        nosauk=atb+'{}'.format(i+1)+'.'+oldf[1]
        new = os.path.join (dir, nosauk)

        dirljaun = os.listdir(dir)
        if nosauk in dirljaun:
            print('')
            print('Jau pastav fails ar tadu nosaukumu!')
            fail=1
            break

        os.rename(old, new)
        print(nosauk)

    i=i+1

if fail!=1:
    print('')
    print('')
    print('Visi faili veiksmigi pardeveti par '+'"'+atb+'"')
    time.sleep(3)

else:
    os._exit(1)