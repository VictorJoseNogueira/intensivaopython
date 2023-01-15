import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# passo 1: entender o desafio
# passo 2: entendimento da area/empresa
# passo 3: obtenção de dados
tabela = pd.read_csv(r"C:\Users\T-GAMER\Desktop\aula intensivão\Aula 4\advertising.csv")
print(tabela)
print(tabela.corr())
print(tabela.info())


# passo 4: tratamento de dados
#nesse exercicio essa etapa ja foi feita pelo lira

#criar grafico
sns.heatmap(tabela.corr(), cmap='Greens', annot=True)
#exibir grafico
plt.show()
# passo 5: analise exploratoria
y = tabela['Vendas']
x = tabela[['TV', 'Radio', 'Jornal']]
# y = quem quero prever x resto




# passo 6: modelagem + algoritimo(IA se necessario )
# passo 7: interpretação de resultados