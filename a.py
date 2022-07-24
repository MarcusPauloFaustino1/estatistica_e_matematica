import pandas as pd 
import numpy as np 






'''a) Organize uma tabela de frequência para as classes.'''



linhas = '28|---29 29|---30 30|---31 31|---32 32|---33 33|---34 34|--|35'.split()

colunas = 'Temperaturas(°C) Frequência_Total(nºdias) Frequência_Relativa'.split()

dados = [1, 2, 3, 3, 2, 4, 6]

relativa = []

for i in range(len(dados)):
    relativa.append(dados[i] / sum(dados))

percentil = []

for i in range(len(relativa)):
    percentil.append(relativa[i]*100)

table = pd.DataFrame()

table['Temperatura (°C)'] = linhas

table['Frequência Absoluta'] = dados

table['Frequencia Relativa'] = relativa

table['%'] = percentil
    
print(f'\n{"="*73}\n')    
print(table)
print(f'\n{"="*73}\n') 