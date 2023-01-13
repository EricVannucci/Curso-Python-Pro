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
