# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
# que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

from math import ceil
from math import floor

print('##### \033[96mLOJA DE TINTAS\033[m #####')

area = int(input('\nInforme em metros quadrados a área a ser pintada: '))
area_com_folga = area * 1.1
cobertura = (area_com_folga/6)
lata = ceil(cobertura/18)
galao = ceil(cobertura/3.6)
lata_misto = floor(cobertura/18)
cobertura_faltante = cobertura % lata
galao_misto = ceil(cobertura_faltante/3.6)

print(f'Para pintar a área de {area}m² será necessário {cobertura:.1f} litros de tinta.')
print(f'\nUsando apenas latas, será necessário {lata} lata(s) no valor de R${lata*80:.2f}')
print(f'Usando apenas galões, será necessário {galao} galão(ões) no valor de R${galao*25:.2f}')
print(f'Usando latas e galões, será necessário {lata_misto} lata(s) e {galao_misto} galão(ões)'
      f' no valor de R${(lata_misto*80)+(galao_misto*25)}')
