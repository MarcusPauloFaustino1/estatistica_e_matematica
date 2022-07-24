import matplotlib.pyplot as plt


'''b) Para cada semana, faça um gráfico de linha, para acompanhar a evolução da temperatura.'''

dias = 'Dom Seg Ter Qua Qui Sex Sab'.split()
semana_1 = [30, 32, 31.5, 31, 33, 34, 33]
semana_2 = [32, 30, 28, 29, 30.5, 31, 29]
semana_3 = [33, 34, 35, 35, 34.5, 34, 33]

plt.title('Evolução da Temperatura (por semanas)', fontweight='bold', fontsize=14)

plt.plot(dias, semana_1, 'bo')
plt.plot(dias, semana_1,  color='blue', label='Semana 1')

plt.plot(dias, semana_2, 'go')
plt.plot(dias, semana_2, color='green', label='Semana 2')

plt.plot(dias, semana_3, 'ro')
plt.plot(dias, semana_3, '--', color='red',label='Semana 3')

plt.xlabel('Dias da Semana', fontsize=12)
plt.ylabel('Temperatura em °C', fontsize=12)

plt.legend()
plt.show()