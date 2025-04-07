import random
from time import sleep
from termcolor import colored
# -----------------------------
print(colored('-=-' * 7, 'yellow'))
print(colored('{:-^20}', 'yellow').format('Desafio 45'))
print(colored('-=-' * 7, 'yellow'))
# --------------------------------------------------------------
print(colored('Bem-Vindo ao Duelo Mortal', 'red'))
sleep(1)
#--------------------------------------------------------------------------------
while True:
    Nome = str(input(colored('Insira Nome De Batalha: ', 'green')))
    print(colored('Você Deseja usar o Nome: {}', 'blue').format(str(Nome)))
#--------------------------------------------------------------------------------------------
    while True:
        SoN = str(input(colored('Sim Ou Não: ', 'green'))).capitalize()
        if SoN == ('Sim') or SoN == ('S'):
#--------------------------------------------------------------------------------------------------------
            while True:
                print(colored('Prepare-se para o Duelo Mortal!!!!', 'light_red'))
                print(colored('Aguarde a Preparações do Campo de batalha', 'yellow'))
                print(colored('........', 'yellow'))
                sleep(1)
                print(colored('Guerreiro {}, Escolha Sua Mão de Ataque!', 'light_yellow').format(Nome))
                Mp = ('👊')
                Mpl = ('🖐️')
                Mt = ('✌️')
                Mão = (Mp, Mpl, Mt)
#------------------------------------------------------------------------------------------------
                while True:
                    Mq = random.choice(Mão)
                    print(colored('Opção 1: {}   Opção 2: {}   Opção 3: {}', 'light_yellow').format(Mp, Mpl, Mt))
                    Op = int(input(colored('Opção: ', 'light_green')))
#----------------------------------------------------------------------------------------------
                    while True:
                        if Op == int(1):
                            Op = Mp
                        elif Op == int(2):
                            Op = Mpl
                        elif Op == int(3):
                            Op = Mt
                        elif Op != (1, 2, 3):
                            print(colored('Porfavor Escolha Uma Opção Correspondente!', 'red'))
                            break
#------------------------------------------------------------------------------
                        while True:
                            if Op == Mp and Mq == Mt:
                                print('vvv')
                                break
                            elif Op == Mpl and Mq == Mp:
                                print('vvv')
                                break
                            elif Op == Mt and Mq == Mpl:
                                print('vvv')
                                break
                            elif Op == Mq:
                                print('empate')
                                break
                            else:
                                print('pppp')

                                exit()
#--------------------------------------------------------------------------------------------
#exit() #Sair do progrma
        elif SoN == ('Não') or SoN == ('Nao') or SoN == ('N'):
            print(colored('Insira o Novo Nome!', 'blue'))
            break  #Sair do Loop interno
        else:
            print(colored('Responda Somente Sim ou Não!', 'red'))
            print(colored('Você Deseja usar o Nome: {}', 'blue').format(str(Nome)))
