"""Faça um Programa que leia três números e mostre o maior deles."""

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))

if n1 >= n2 and n1 >= n3:
    print(f'O número {n1} é o maior número digitado!')
elif n2 >= n1 and n2 >= n3:
    print(f'O número {n2} é o maior número digitado!')
elif n3 >= n1 and n3 >= n2:
    print(f'O número {n3} é o maior número digitado!')
