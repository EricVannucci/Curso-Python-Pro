# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
# quantidades de latas de tinta a serem compradas e o preço total.

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
