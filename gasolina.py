import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gas = pd.read_csv('./gasolina.csv')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gas, x='dia', y='venda', palette='pastel')
  grafico.set(title='Preço gasolina por dia', xlabel='Dia', ylabel='Preço')
  plt.savefig('gasolina.png')