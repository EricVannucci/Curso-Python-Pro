# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a.O produto do dobro do primeiro com metade do segundo.
# b.A soma do triplo do primeiro com o terceiro.
# c.O terceiro elevado ao cubo.

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = float(input('Digite um número real: '))
print(f'O produto do dobro de {n1} com a metade de {n2} é igual a {(n1*2)*(n2/2)}')
print(f'A soma do triplo de {n1} com {n3} é {(n1*3)+n3}')
print(f'{n3} elevado ao cubo é igual a {n3**3}')
