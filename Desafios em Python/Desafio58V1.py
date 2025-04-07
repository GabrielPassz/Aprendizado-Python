#---Biblilotecas---- 
from os import system
from random import randint
from termcolor import colored
from time import sleep
#-----------------------------------
system("cls")
print(colored('-=-' * 7, 'yellow'))
print(colored('{:-^20}', 'yellow').format('Desafio 45'))
print(colored('-=-' * 7, 'yellow'))
#---------------------------------------------------------------
Mq = randint(1, 10)
Jg = int
i = 1
print(colored('Olá, sou o Tony!, Vamos jogar um jogo?','red'))
sleep(1)
print(colored("O obejtivo deste jogo é adivinha em qual numero estou pensando.", 'red'))
sleep(1)
print(colored('Vamos lá!', 'red'))
sleep(1)
print(colored('Deixa-me pensa......', 'red'))
sleep(1)
print(colored('Pronto!', 'red'))
Jg = int(input(colored('Adivinha meu Numero: ', 'red')))
while Jg != Mq:
    i+=1
    Jg = int(input(colored('Adivinha meu Numero: ', 'red')))
print(colored('Oloco meu! Você Acertou!', 'red'))
sleep(1)
print(colored('Meu numero era {}!' 'Você tentou {} vezes para acertar.', 'red').format(Mq, i))