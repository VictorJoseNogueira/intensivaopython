import pyautogui
import pyperclip
from time import sleep
import pandas as pd
# passo 1: entrar no sistema da empresa
pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
sleep(2)
pyautogui.hotkey('ctrl', 't')
sleep(2)
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl', 'v')
pyautogui.PAUSE = 1
pyautogui.press('enter')
sleep(3)
# passo 2: entrar no relatorio
pyautogui.click(x=297, y=302, clicks=1)
pyautogui.doubleClick(x=297, y=302)
sleep(3)
# passo 3: exportar o relatorio
pyautogui.click(x=297, y=302)
sleep(1)
pyautogui.click(x=1072, y=197)
sleep(3)
pyautogui.click(x=836, y=562)
sleep(6)

# passo 4: calcular indicadores
tabela = pd.read_excel(r"C:\Users\T-GAMER\Downloads\Vendas - Dez.xlsx")
#print(tabela)

faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
print(f'faturamento>>>{faturamento}')
print(f'Quantidade>>>>{quantidade}')
# passo 5: enviar email para a diretoria
#abrir o navegador
pyautogui.PAUSE = 1
#entrar no site do email
pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://mail.google.com/mail/u/0/#inbox')
pyautogui.press('enter')
#clicar em novo email
sleep(2)
pyautogui.click(x=88, y=199)
sleep(1)
#escrever email
pyautogui.write('victorvalim1@gmail.com')
pyautogui.press('enter')
pyautogui.press('tab')
pyperclip.copy('Relátorio de faturamento')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
texto = f'''prezado victor, bom dia
o faturamento total do mês de dezembro foi de: R$: {faturamento:,.2f}
a quantidade total de produtos vendidos foi de: {quantidade:,}
att 
victor
email enviado automaticamente'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')
#enviar email