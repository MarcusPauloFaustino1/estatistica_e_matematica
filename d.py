'''d) Calcule a média para cada semana.'''

semana_1 = [30, 32, 31.5, 31, 33, 34, 33]
semana_2 = [32, 30, 28, 29, 30.5, 31, 29]
semana_3 = [33, 34, 35, 35, 34.5, 34.02, 33.02]

media_1 = sum(semana_1) / len(semana_1)
media_2 = sum(semana_2) / len(semana_2)
media_3 = sum(semana_3) / len(semana_3)

print(f'{"="*43}')
print(f'Média de temperatura da semana 1: \033[1m\033[94m{media_1:.2f} °C')
print(f'\033[0mMédia de temperatura da semana 2: \033[1m\033[94m{media_2:.2f} °C')
print(f'\033[0mMédia de temperatura da semana 3: \033[1m\033[94m{media_3:.2f} °C')
print(f'\033[0m{"="*43}')