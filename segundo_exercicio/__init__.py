# Passo 1: Importar a base de dados
import pandas as pd
import plotly.express as px
tabela = pd.read_csv(r"C:\Users\T-GAMER\Desktop\aula intensivão\Aula 2\telecom_users.csv")

# Passo 2: Visualizar a base de dados
tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela)
# - Entender quais as informações tão disponíveis
# - Descobrir as cagadas da base de dados
# Passo 3: Tratamento de dados
# - Valores que estão reconhecidos de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# - Valores vazios
# deletando as colunas vazias
# axis = 0 _> linha ou axis = 1 _> coluna
tabela = tabela.dropna(how="all", axis=1)
# deletando as linhas vazias
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())
# Passo 4: Análise Inicial
# Como estão os nossos cancelamentos?
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

#1º etapa criar grafico
#criar um grafico para cada coluna
#for coluna in tabela.columns:
 #   grafico = px.histogram(tabela, x=coluna, color='Churn', text_auto=True)

    #2º etapa mostrar grafico
  #  grafico.show()

resumo = '''
- clientes com mais familiares tendem a ter menos cancelamento
    - promoções diferenciadas para mais pessoas da mesma familia
- clientes nos primeiros meses tem uma tendencia muito MUITO a cacelarem
    - pode ser algum marketing muito agressivo
    - experiencia nos primeiros meses ruins
    -planos mais baratos nos primeiros anos
- clientes com mais serviços cancelam menos
    - clientes com serviço de fibra cancelam mais do que os que nao tem
    - clientes sem serviço de segurança online tendem a cancelare mais
    - clientes sem serviço de backup online cancelam mais 
    - clientes sem serviço de proteção ao equipamentos tendem a cancelarem mais
    - clientes sem suporte tecnico cancelam mais 
    
        * podemos oferecer maior quantidade de produtos com preço reduzido ou zerado
        
- Quase todos cancelamentos estao no contrato mensal
    * oferecer descontos nos outros planos

- clientes que pagam no boleto tendem a cancelar mais
'''

print(resumo)