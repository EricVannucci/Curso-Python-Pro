idade = int(input('Digite sua idade: '))
if idade < 18:
    print(f'{idade} anos é menor de idade!')
elif idade >= 65:
    print(f'{idade} anos é idoso!')
else:
    print(f'{idade} anos é maior de idade!')
