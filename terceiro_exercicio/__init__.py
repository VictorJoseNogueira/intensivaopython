import pandas as pd
import pyautogui
import pyautogui as py
import pyperclip
from time import sleep
from selenium import webdriver
navegador = webdriver.Chrome()
sleep(2)
navegador.get(r'https://www.google.com/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dolar')


#1: conferir cotações
    #1.1: cotação do ouro
    #1.2: cotação do euro
    #1.3: cotação do dolar
#2: exportar base de dados
#3: alterar valores da base de dados
#4: exportar base de dados
