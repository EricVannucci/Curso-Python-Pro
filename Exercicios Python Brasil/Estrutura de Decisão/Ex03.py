"""Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido"""

sexo = str(input('Digite seu sexo [M/F]: ')).lower().strip()[0]
if sexo == 'm':
    print('Sexo Masculino')
elif sexo == 'f':
    print('Sexo Feminino')
else:
    print('Sexo Inválido')
