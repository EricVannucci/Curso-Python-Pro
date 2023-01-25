"""Faça um Programa que leia três números e mostre o maior e o menor deles."""

print(30 * '*')
print(f'\033[96m{"COMPARADOR DE NÚMEROS":^30}\033[m')
print(30 * '*')

n1 = int(input('\nDigite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

maior = menor = n1
# testanto maior número

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

# testanto menor número

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f'\nO maior número é {maior}')
print(f'O menor número é {menor}')
