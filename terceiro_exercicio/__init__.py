from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys








print(f'{float(cotacao_euro):.2f}')
print(f'{float(cotacao_dolar):.2f}')

#1: conferir cotações
    #1.1: cotação do dolar
navegador = webdriver.Chrome()
navegador.get(r'https://www.google.com/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dolar')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

    #1.2: cotação do euro
navegador.find_element('xpath', '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').click()
navegador.find_element('xpath', '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').clear()
navegador.find_element('xpath', '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').send_keys('cotação euro')
navegador.find_element('xpath', '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
cotacao_euro
    #1.3: cotação do ouro
navegador.find_element('xpath', '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').click()
navegador.find_element('xpath', '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').clear()
navegador.find_element('xpath', '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').send_keys('cotação ouro')
navegador.find_element('xpath', '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_ouro = navegador.find_element('xpath', )
#2: exportar base de dados
#3: alterar valores da base de dados
#4: exportar base de dados
