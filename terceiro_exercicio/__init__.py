import pandas as pd
import pyautogui
import pyautogui as py
import pyperclip
from time import sleep
from selenium import webdriver
navegador = webdriver.Chrome()
sleep(5)
navegador.get(r'https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar&rlz=1C1ONGR_pt-PTBR1005BR1005&oq=cota%C3%A7&aqs=chrome.1.69i57j0i67i131i433j0i67i433j0i67i131i433l2j0i131i433i512j0i433i512j0i67i131i433j0i131i433j0i67i433.2207j1j7&sourceid=chrome&ie=UTF-8')


#1: conferir cotações
    #1.1: cotação do ouro
    #1.2: cotação do euro
    #1.3: cotação do dolar
#2: exportar base de dados
#3: alterar valores da base de dados
#4: exportar base de dados
