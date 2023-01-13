#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

print('********** Cálculo Salarial **********')
salario = float(input('Digite o salário por hora: R$ '))
horas = float(input('Digite a quantidade de horas trabalhadas: '))
print(f'Valor a receber será de R$ {salario*horas:.2f}')
