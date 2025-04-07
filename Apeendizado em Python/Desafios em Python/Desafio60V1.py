#bibliotecas-------------------------------
from time import sleep
from os import system
from termcolor import colored
# -----------------------------
system('cls')
print(colored('-=-' * 7, 'yellow'))
print(colored('{:-^20}', 'yellow').format('Desafio 60'))
print(colored('-=-' * 7, 'yellow'))
#--------------------------------------------------------
N = int(input('Digitir um numero para calcular seu fatorial: '))
C = N
F = 1
print('Calculando {}! = '.format(N), end='')
while C > 0:
    print('{}'.format(C), end='')
    print(' x ' if C > 1 else ' = ', end='')
    F *= C
    C -= 1
print('{}'.format(F))