import os
import random
import shutil
from winreg import *

import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

def laiks():
    laiks = time.localtime()
    palaiks = time.strftime("%H:%M:%S", laiks)
    print('Laiks: '+palaiks)
    print('')

url=r'https://drive.google.com/drive/folders/13cdJcLxUeCBtcs1BYVlfGJotJ3SaqdUj?usp=sharing'

options = webdriver.ChromeOptions()
options.headless = False
driver = uc.Chrome(use_subprocess=True,options=options)

driver.minimize_window()

print('Pirma stadija:')
laiks()

driver.get(url)
driver.implicitly_wait(20)
time.sleep(2)

driver.set_window_position(0, 2000, windowHandle='current')
poga=driver.find_element(By.XPATH,'//*[@id="drive_main_page"]/div/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div/div[3]')
driver.implicitly_wait(10)
poga.click()

#gifu skaitam
gifi=driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[2]/div[2]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div').text
driver.implicitly_wait(10)

gifi=gifi.splitlines()

gifusk=0
i=0
for j in gifi:
    if 'MB' in gifi[i]:
        gifusk=gifusk+1

    i=i+1

#dir iegusana
dirp= os.getcwd()
dirpl= os.listdir(dirp)

#lejupielades atrasanasn vieta
with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]

#gifa izvele
nr=random.randint(1,gifusk)
gifv='gifs{}'.format(nr)+'.gif'
gifnr = os.path.join(Downloads, gifv)
gifnrnew=os.path.join(dirp, gifv)

print('Otra stadija:')
laiks()

#gifa jau esamibas parbaude
if gifv in dirpl:
    os.startfile(gifnrnew)

else:
    #lejupielade
    gifs=driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[2]/div[2]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz[{}]/div/div/div'.format(nr))
    driver.implicitly_wait(10)
    gifs.click()

    lade=driver.find_element(By.XPATH,'/html/body/div[11]/div[4]/div/div[3]/div[2]/div[2]/div[3]')
    driver.implicitly_wait(10)
    time.sleep(1)
    lade.click()

    print('')
    print('Gifa Iegusanas processa sakums: ')
    laiks()

    Downloadsl=os.listdir(Downloads)
    while gifv not in Downloadsl:
        Downloadsl = os.listdir(Downloads)

    print('Gifa iegusanas processa beigas: ')
    laiks()

    #gifa kopesana un atversana
    shutil.move(gifnr,dirp)
    os.startfile(gifnrnew)

#terminatus
time.sleep(0.1)
driver.quit()
time.sleep(0.1)
os._exit(407)
