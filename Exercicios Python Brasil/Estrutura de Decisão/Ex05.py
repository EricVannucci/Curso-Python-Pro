"""Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez."""

print('\033[96m----> Boletim Escolar <----\033[m')
nome = str(input('Digite o nome do aluno: ')).strip().title()
nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input('Informe a segunda nota do aluno: '))
media = (nota1 + nota2) / 2

if media == 10:
    print(f'O aluno {nome} obteve média {media} e está \033[34mAPROVADO COM DISTINÇÃO\033[m')
elif media >= 7:
    print(f'O aluno {nome} obteve média {media} e está \033[32mAPROVADO\033[m.')
else:
    print(f'O aluno {nome} obteve média {media} e está \033[31mREPROVADO\033[m.')
