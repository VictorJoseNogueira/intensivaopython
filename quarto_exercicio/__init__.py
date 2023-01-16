import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
# passo 1: entender o desafio
# passo 2: entendimento da area/empresa
# passo 3: obtenção de dados
tabela = pd.read_csv(r"C:\Users\T-GAMER\Desktop\aula intensivão\Aula 4\advertising.csv")

# passo 4: tratamento de dados
#nesse exercicio essa etapa ja foi feita pelo lira

#criar grafico
#sns.heatmap(tabela.corr(), cmap='Greens', annot=True)
#exibir grafico
#plt.show()
# passo 5: analise exploratoria
y = tabela['Vendas']
x = tabela[['TV', 'Radio', 'Jornal']]
# y = quem quero prever x resto dados de treino e dados de teste

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)#random teste apenas para aprender

#criar IA
modelo_regressao = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

#treinar IA
modelo_regressao.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

previsao_linear = modelo_regressao.predict(x_teste)
previsao_arvore = modelo_arvoredecisao.predict(x_teste)
print(r2_score(y_teste, previsao_linear))
print(r2_score(y_teste, previsao_arvore))

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar['y_teste'] = y_teste
tabela_auxiliar['Previsão_arvore'] = previsao_arvore
tabela_auxiliar['Previsão_linear'] = previsao_linear

sns.lineplot(tabela_auxiliar)
print(tabela_auxiliar)
plt.show()

novatabela = pd.read_csv(r"C:\Users\T-GAMER\Desktop\aula intensivão\Aula 4\novos.csv")
print(novatabela)
previsao_linear2 = modelo_regressao.predict(novatabela)
previsao_arvore2 = modelo_arvoredecisao.predict(novatabela)
print(previsao_arvore2)
print(previsao_linear2)

# passo 6: modelagem + algoritimo(IA se necessario )

# passo 7: interpretação de resultados