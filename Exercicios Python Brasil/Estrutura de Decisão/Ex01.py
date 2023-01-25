"""Faça um Programa que peça dois números e imprima o maior deles."""

n1 = float(input('Digite um número: '))
n2 = float(input('Digite agora outro número: '))

if n1 > n2:
    print(f'O número digitado primeiro ({n1}) é maior que o segundo ({n2})')
else:
    print(f'O número digitado primeiro ({n1}) é menor que o segundo ({n2})')
