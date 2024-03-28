import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('./gasolina.csv')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=data, x='dia', y='venda', palette='dark')
  grafico.set(title='História do preço da gasolina por dia', xlabel='Dia', ylabel='Preço')
  plt.savefig('gasolina.png')