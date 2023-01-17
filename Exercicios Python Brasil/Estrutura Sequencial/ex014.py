# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário
# de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
# de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o
# excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o
# valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

print("<<< \033[96mControle de pesca\033[m >>>\n")
peso = float(input("Informe o peso total da pesca em quilos: "))
multa = 4
peso_reg = 50
if peso > peso_reg:
    print("\033[31mExcedeu o peso máximo regulamentado, deverá ser pago multa por peso excedido!")
    print(f"O valor da multa a ser pago é: R${(peso-peso_reg)*multa:.2f}")
else:
    print("\033[32mPeso dentro do regulamentado, não haverá multa.")