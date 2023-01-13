# Passo 1: Importar a base de dados
import pandas as pd

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