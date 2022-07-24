import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

'''e) Obter o box-plot para cada semana.'''

data = {
    'Semana 1' : [30, 32, 31.5, 31, 33, 34, 33],
    'Semana 2' : [32, 30, 28, 29, 30.5, 31, 29],
    'Semana 3' : [33, 34, 35, 35, 34.5, 34.02, 33.02],
    
}

df_1 = pd.DataFrame(data)

plt.title('Boxplot das Temperaturas por Semanas', fontweight='bold', fontsize=14)
plt.ylabel('Temperaturas em °C',fontsize=12)

boxplot = df_1.boxplot()


'''e) Obter o box-plot para toda série'''

serie = {'Série' : [30, 32, 31.5, 31, 33, 34, 33, 32, 30, 28, 29, 30.5, 31, 29, 33, 34, 35, 35, 34.5, 34, 33]}

df_2 = pd.DataFrame(serie)

plt.title('Boxplot das Temperaturas por Semanas', fontweight='bold', fontsize=14)
plt.ylabel('Temperaturas em °C',fontsize=12)

boxplot = df_2.boxplot()