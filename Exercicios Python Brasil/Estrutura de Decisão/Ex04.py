"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

letra = input('Digite uma letra: ').strip().upper()[0]
if letra.isalpha():
    if letra in {'A', 'E', 'I', 'O', 'U'}:
        print(f'A letra \033[96m{letra}\033[m é uma VOGAL!')
    else:
        print(f'A letra \033[96m{letra}\033[m é uma CONSOANTE!')
else:
    print(f'\033[31m{letra} NÃO é uma letra!')
