from bs4 import BeautifulSoup as BS
import requests

html=requests.get('https://www.r64vsk.lv/').text
soup=BS(html, 'lxml')

izmainas=soup.select('div.r64-events')
linijas=izmainas[0].text.splitlines()

beigas=0
kopbeigas=0
cikls=1

def izmainass():
    global linijas
    global cikls
    global beigas
    global izmsk
    
    if izmsk>1: 
        print('Izmainas({}): '.format(cikls))
        print('')
        
    else:
        print('Izmainas: ')
        print('')
    
    #Tuksumu parbaude
    while 1<2:
        if ',' not in linijas[0]:
            linijas.pop(0)
        else:
            break
    
    #izmainu paradisana
    if cikls==1:
        i=0
        
    else:
        i=beigas
        
    while daudz>i:
        if cikls==1:
            if i>0 and 'diena,' in linijas[i]:
                beigas=i
                break
                
        if len(linijas[i])==1:
            break
            
        print('#'+linijas[i])
        i=i+1
    
def kopsavilkums():
    global cikls
    global beigas
    global kopbeigas
    global linijas
    global izmsk
    
    
    if izmsk>1: 
        print('Kopsavilkums({}): '.format(cikls))
        print('')
        
    else:
        print('Kopsavilkums: ')
        print('')
    
    #Diena
    print('Diena: ')
    diensk=linijas[kopbeigas].split()
    for j in linijas[kopbeigas]:
        if j.isdigit():
            diena=diensk[0]
            diena=diena.replace(',',', ')
        
        else:
            diena=diensk[0]+' '+diensk[1] 
        
        if '-' in diena:
            diena=diena.split('-')
            diena.pop(1)
            diena=diena[0]
            
    print('#'+diena)
    print('')
    
    #Skolotājas
    print('Skolā nav: ')
    if 'sk.Ozols' in linijas[kopbeigas]:
        print('#'+'sk.Ozols')

    if 'sk.Upesleja' in linijas[kopbeigas]:
        print('#'+'sk.Upesleja')

    if 'sk.Petere' in linijas[kopbeigas]:
        print('#'+'sk.Petere')

    if 'sk.Bukovskis' in linijas[kopbeigas]:
        print('#'+'sk.Bukovskis')

    if 'sk.Saliņš' in linijas[kopbeigas]:
        print('#'+'sk.Saliņš')

    if 'sk.Feldmanis' in linijas[kopbeigas]:
        print('#'+'sk.Feldmanis')

    if 'sk.Skrupska' in linijas[kopbeigas]:
        print('#'+'sk.Skrupska')

    if 'sk.Sukurs' in linijas[kopbeigas]:
        print('#'+'sk.Sukurs')

    if 'sk.Zinberga' in linijas[kopbeigas]:
        print('#'+'sk.Zinberga')

    if 'sk.Zīverts' in linijas[kopbeigas]:
        print('#'+'sk.Zīverts')

    if 'sk.Vdovičenko' in linijas[kopbeigas]:
        print('#'+'sk.Vdovičenko')

    if 'sk.Oga' in linijas[kopbeigas]: #dizains
        print('#'+'sk.Oga'+' (dizains)')

    if 'sk.Reimandova' in linijas[kopbeigas]: #dizains
        print('#' + 'sk.Reimandova' + ' (dizains)')

    print('')
    #Stundas
    print('Stundas: ')
    if cikls==1:
        i=0
    else:
        i=kopbeigas
        
    while daudz>i:
        if cikls==1:
            if i>0 and 'diena,' in linijas[i]:
                break
        
        if '12.DIT' in linijas[i]:
            if 'dizains' or 'māksla' in linijas[i]:
                print('#'+linijas[i]+' (dizains)')

            else:
                print('#' + linijas[i])
            
        i=i+1
    
    kopbeigas=beigas
    cikls=cikls+1

#izmainu skaits
izmsk=0

i=0
for j in linijas:
    if 'diena,' in linijas[i]:
        izmsk=izmsk+1
        
    i=i+1

#liniju daudzums
daudz=0
for j in linijas:
    daudz=daudz+1

#Izmainu paradisana
izmainass()
print('_____________________________________________________________________')
kopsavilkums()
print('')

if izmsk>1:
    print('=====================================================================')
    izmainass()
    print('_____________________________________________________________________')
    kopsavilkums()
    print('')

#iziesana
while 2>1:
    iziesana=0





