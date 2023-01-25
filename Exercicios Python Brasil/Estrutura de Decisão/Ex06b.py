"""Faça um Programa que leia três números e mostre o maior deles."""

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))

maior = n1

if n2 > maior:
    maior = n2
elif n3 > maior:
    maior = n3

print(f'O maior número digitado é {maior}')
