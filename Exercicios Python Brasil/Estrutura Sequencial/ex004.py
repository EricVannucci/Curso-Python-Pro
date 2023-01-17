#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nome = str(input('Digite o nome completo do aluno: ')).strip().title()
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
n3 = float(input('Digite a terceira nota do aluno: '))
n4 = float(input('Digite a quarta nota do aluno: '))
print(f'A média bimestral do aluno {nome} foi: {(n1+n2+n3+n4)/4:.2f}')
