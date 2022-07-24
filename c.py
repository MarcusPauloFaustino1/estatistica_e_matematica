'''c) Calcule a média de toda a série.'''

serie = [30, 32, 31.5, 31, 33, 34, 33, 32, 30, 28, 29, 30.5, 31, 29, 33, 34, 35, 35, 34.5, 34, 33]

media = sum(serie) / len(serie)


print(f'{"="*55}')
print(f'\n\nA média de temperatura de toda a série é de \033[1m\033[94m{media:.2f} °C\n\n')
print(f'\033[0m{"="*55}')