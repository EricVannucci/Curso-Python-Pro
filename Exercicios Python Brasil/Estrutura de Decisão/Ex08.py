"""Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato."""

print(f"\033[31m{'LOJAS AMERICANAS'::^50}\033[m")
print('\nDEPARTAMENTO DE INFORMÁTICA')
print('IMPRESSORAS:')

valor1 = float(input('Informe o primeiro valor: R$ '))
valor2 = float(input('Informe o segundo valor: R$ '))
valor3 = float(input('Informe o terceiro valor: R$ '))
menor = valor1

if valor2 < menor:
    menor = valor2
    print('\nSegunda impressora é a mais vantajosa!')
elif valor3 < menor:
    menor = valor3
    print('\nTerceira impressora é a mais vantajosa!')
else:
    print('\nPrimeira impressora é a mais vantajosa!')
