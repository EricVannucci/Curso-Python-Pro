def classificar(idade, nome):
    if idade < 18:
        return f'{nome} tem {idade} anos e é menor de idade!'
    elif idade >= 65:
        return f'{nome} tem {idade} anos e é idoso!'
    else:
        return f'{nome} tem {idade} anos e é maior de idade!'
