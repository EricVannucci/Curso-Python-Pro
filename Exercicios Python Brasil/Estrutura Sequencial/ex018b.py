# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um
# link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando
# este link (em minutos).

print('\033[36m -> Tempo de Download <- \033[m')
arquivo = float(input('\nInforme o tamanho do arquivo a ser baixado em megabytes (MB): '))
velocidade = float(input('Informe a velocidade da internet em megabytes por segundo (Mbps): '))
tempo_download = arquivo / (velocidade / 8)  # divisão por 8 é: 8 bits equivalem a 1 ‘byte’.
mintutos = tempo_download // 60
segundos = tempo_download % 60

print(f'Tempo de download deste arquivo de {arquivo} MB, será de aproximadamente '
      f'{mintutos:.0f} minutos e {segundos:.0f} segundos.')
