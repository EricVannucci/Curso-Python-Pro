print("<<< \033[96mControle de pesca\033[m >>>\n")
peso = float(input("Informe o peso total da pesca em quilos: "))
multa = 4
peso_reg = 50
if peso > peso_reg:
    print("\033[31mExcedeu o peso máximo regulamentado, deverá ser pago multa por peso excedido!")
    print(f"O valor da multa a ser pago é: R${(peso-peso_reg)*multa:.2f}")
else:
    print("\033[32mPeso dentro do regulamentado, não haverá multa.")