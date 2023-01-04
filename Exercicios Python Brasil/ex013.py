print("Calculadora de peso ideal")
print(25*"\033[96m-")
sexo = str(input("\033[mInforme seu sexo [M/F]: ")).lower().strip()
while sexo not in 'mf':
    sexo = str(input('\033[31mResposta inválida\033[m, informe seu sexo usando "M" para MASCULINO '
                     'e "F" para FEMININO: ')).lower().strip()
if sexo == 'f':
    h = float(input("Qual a sua altura? "))
    peso = (62.1*h)-44.7
    print(f"Seu peso ideal é {peso:.2f} kg")
elif sexo == 'm':
    h = float(input("Qual a sua altura? "))
    peso = (72.7*h)-58
    print(f"Seu peso ideal é {peso:.2f} Kg")
