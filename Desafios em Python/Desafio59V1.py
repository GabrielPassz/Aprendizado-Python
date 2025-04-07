#bibliotecas-------------------------------
from time import sleep
from os import system
from termcolor import colored
# -----------------------------
system('cls')
print(colored('-=-' * 7, 'yellow'))
print(colored('{:-^20}', 'yellow').format('Desafio 59'))
print(colored('-=-' * 7, 'yellow'))
#Variaveis-------------------------------------------------------------
Menu = 0
#--------------------------------------------------------------
print(colored('Olá, sou Tony!' '\nIrei Solicitar dois valores para você usa de algumas formas!', 'red'))
sleep(1)
print(colored('Então Aguarde o processamento!', 'red'))
sleep(1.2)
Numb1 = int(input(colored('Insira o seu Primeiro Numero: ', 'yellow')))
Numb2 = int(input(colored('Insira o seu Segundo Numero: ', 'yellow')))
sleep(1.2)
print(colored('Processando.....', 'red'))
sleep(1.2)
print(colored('Olá, novamente, entre as opções abaixo escolha oque voce gostaria de fazer como seu numero.', 'red'))
sleep(1)
while Menu != 5:
    sleep(1)
    print(colored('|[1]- Somar| |[2] - Multiplicar| |[3] - Maior| |[4] - Novos Numeros| |[5] - Sair do Programa|', 'yellow'))
    Menu = int(input(colored('Opção: ', 'yellow')))
    if Menu == 1:
        Soma = Numb1 + Numb2
        print(colored('A Soma dos dois Numeros é: {}', 'red').format(Soma))
    elif Menu == 2:
        Mult = Numb1 * Numb2
        print(colored('A Multiplicarção dos Numeros é: {}', 'red').format(Mult))
    elif Menu == 3:
        if Numb1 > Numb2:
            print(colored('O Numero {} e Maior que {}.', 'red').format(Numb1, Numb2))
        else:
            print(colored('O Numero {} e Maior que {}.', 'red').format(Numb2, Numb1))
    elif Menu == 4:
        Numb1 = int(input(colored('Insira o seu Primeiro Numero: ', 'yellow')))
        Numb2 = int(input(colored('Insira o seu Segundo Numero: ', 'yellow')))
    elif Menu == 5:
        print(colored('Finalizando.....', 'red'))
    else:
        print(colored('Opção Invalida!', 'red'))
print(colored('Volte Sempre!', 'red'))