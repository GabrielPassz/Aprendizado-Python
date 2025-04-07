from os import system
from time import sleep
from termcolor import colored
# -----------------------------
system('cls')
print(colored('-=-' * 7, 'yellow'))
print(colored('{:-^20}', 'yellow').format('Desafio 42'))
print(colored('-=-' * 7, 'yellow'))
#--------------------------------------------------------------
R1 = float(input('Insira o Comprimento do Priemiro Reta: '))
R2 = float(input('Insira o Comprimento do Segundo Reta: '))
R3 = float(input('Insira o Comprimento do Terceiro Reta: '))
M = R1
if R2 > M:
    M = R2
if R3 > M:
    M = R3
if M == R1:
    S = (R2 + R3)
if M == R2:
    S = (R1 + R3)
if M == R3:
    S = (R1 + R2)
print('Analisando!...')
sleep(2)
if M < S:
    print('É possivel Forma um Triângulo!')
    if R1 == R2 == R3:
        print('Esse triangulo é Equilátero!')
    if R1 == R2 != R3 or R2 == R3 != R1 or R3 == R1 != R2:
        print('Esse Triangulo é Isosceles')
    if R1 != R2 != R3:
        print('Esse triangulo é Escaleno!')
else:
    print('Não é Possivel Forma um Triângulo!')