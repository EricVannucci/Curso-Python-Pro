from math import ceil
print('>>>> \033[96mLoja de Tintas\033[m <<<<')

altura = int(input('Qual a altura da parede que deseja pintar? '))
largura = int(input('Qual a largura da parede que deseja pintar? '))
area = altura*largura
cobertura = area/3
latas = ceil(cobertura/18)
valor = latas*80

print(f'Para printar os {area}m² desejados, você irá precisar de {latas} lata(s) de tinta '
      f'no valor de R${valor:.2f}.')
