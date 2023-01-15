from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import datetime as dt
x = dt.date.today()
print(x)








#1: conferir cotações
    #1.1: cotação do dolar
navegador = webdriver.Chrome()
navegador.get(r'https://www.google.com/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dolar')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

    #1.2: cotação do euro
navegador = webdriver.Chrome()
navegador.get(r'https://www.google.com/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
   #1.3: cotação do ouro
navegador = webdriver.Chrome()
navegador.get(r'https://www.google.com/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('https://www.melhorcambio.com/ouro-hoje')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
navegador.find_element('xpath', '//*[@id="rso"]/div[1]/div/div/div/div[1]/div/div/div[1]/div/a/h3').click()
cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",", ".")
cotacao_ouro = float(cotacao_ouro)
cotacao_euro = float(cotacao_euro)
cotacao_dolar = float(cotacao_dolar)


navegador.quit()



#2: exportar base de dados
tabela = pd.read_excel('Produtos.xlsx')


#3: alterar valores da base de dados
tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(cotacao_dolar)
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(cotacao_euro)
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(cotacao_ouro)
#preço de compra = preço original X cotação
tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']

#preço de venda = preço de compra X margem
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

#formatando
tabela['Preço de Compra'] = tabela['Preço de Compra'].map("RS{:.2f}".format)
tabela['Preço de Venda'] = tabela['Preço de Venda'].map("RS{:.2f}".format)
tabela['Cotação'] = tabela['Cotação'].map("R${:.2f}".format)
print(x)


#4: exportar base de dados
tabela.to_excel(f'produtos{x}.xlsx', index=False)