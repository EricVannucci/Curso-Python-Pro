# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
# quantidades de latas de tinta a serem compradas e o preço total.

from math import ceil
print("<<< \033[31mCalculadora de tintas\033[m >>>\n")

altura = float(input("Informe a medida em metros da altura da parede: "))
largura = float(input("Informe a medida em metros da largura da parede: "))
m2 = altura*largura
print(f'Sua parede tem {m2:.1f} metros quadrados.')

rendimento_tinta = m2/3
print(f'Você precisará de {rendimento_tinta:.1f} litros de tinta.')

galoes = rendimento_tinta/18
print(f'Você precisará de {ceil(galoes)} galões no valor de R${ceil(galoes)*18:.2f}.')
