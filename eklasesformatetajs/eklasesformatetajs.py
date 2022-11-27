#eklases skolenu nosaukumu formatejums (1 vards 1 uzvards; 2 vardi 1 uzvards)

import os
import time

dir=os.getcwd()
list=os.listdir(dir)

print('Teksta faila nosaukums:')
while 1<2:
    inp=input('>')
    if inp+'.txt' in list:
        break

    else:
        print("Teksta fails '"+inp+"'"+' netika atrasts!')

path=dir+'\\'+inp+'.txt'
jaunf=dir+'\\'+inp+'FORMATETS.txt'

fails=open(path,'r')
failsjaun=open(jaunf,'w')

skoleni= fails.readlines()

sk=len(skoleni)
i=0
while i<sk:
    skolens=skoleni[i].split(',')
    skolens=skolens[0]
    skolens=skolens.split(' ')
    skolens.pop(-1)

    if i<sk-1:
        if len(skolens)>2:
            skolens = skolens[1] + ' ' + skolens[2]+ ' ' +skolens[0]+'\n'

        else:
            skolens = skolens[1] + ' ' + skolens[0]+'\n'

    else:
        if len(skolens) > 2:
            skolens = skolens[1] + ' ' + skolens[2] + skolens[0]

        else:
            skolens = skolens[1] + ' ' + skolens[0]

    failsjaun.write(skolens)

    i=i+1

fails.close()
failsjaun.close()

print(' ')
print('Formatejums pabeigts!')

time.sleep(3)