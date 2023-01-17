# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
# o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

print("<<< \033[95mCalculadora de Salario Líquido\033[m >>>\n")
salario_hora = float(input("Informe o valor da Hora/Trabalho: R$"))
hora_trabalhada = float(input("Informe quantas horas foram trabalhadas no mês: "))
salario_bruto = salario_hora*hora_trabalhada
ir = salario_bruto*11/100
inss = salario_bruto*8/100
sind = salario_bruto*5/100
salario_liquido = salario_bruto-(ir+inss+sind)
print(f"\nSalário Bruto Mensal: R${salario_bruto:.2f}")
print(f"Desconto IR (11%): R${ir:.2f}")
print(f"Desconto INSS (8%): R${inss:.2f}")
print(f"Desconto Sindical (5%): R${sind:.2f}")
print(35*"-")
print(f"Salário Líquido: R${salario_liquido:.2f}")
