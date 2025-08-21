#Jogo da velha

import os
import random
from colorama import Fore, Back, Style

jogarNovamente = "s"
jogadas = 0
quemJoga = 2 # 1 = CPU || 2 = Jogador
maxJogadas = 9
vitoria = "n"
velha = [[" "," "," "],[" "," "," "],[" "," "," "]]

def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input("Linha: "))
            c = int(input("Coluna: "))
        except ValueError:
            print("Valor inválido!")
            return
        if velha[l][c] == " ":
            velha[l][c] = "X"
            quemJoga = 1
            jogadas += 1
        else:
            print("Campo já preenchido!")
            return

def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while velha[l][c] != " ":
            l = random.randrange(0,3)
            c = random.randrange(0,3)
        velha[l][c] = "O"
        quemJoga = 2
        jogadas += 1

def verificarVitoria():
    global velha
    vitoria = "n"
    simbolos = ["X","O"]
    for s in simbolos:
        vitoria = "n"
        #Verificar linhas
        for il in range(3):
            soma = 0
            for ic in range(3):
                if velha[il][ic] == s:
                    soma += 1
            if soma == 3:
                vitoria = "s"
                break
        if vitoria == "s":
            break

        #verificar colunas
        for ic in range(3):
            soma = 0
            for il in range(3):
                if velha[il][ic] == s:
                    soma += 1
            if soma == 3:
                vitoria = "s"
                break
        if vitoria == "s":
            break

        #verifica diagonal 1
        soma = 0
        for idiag in range(3):
            if velha[idiag][idiag] == s:
                soma += 1
        if soma == 3:
            vitoria = "s"
            break

        #verifica diagonal 2
        soma = 0
        for idiagl in range(3):
            idiagc = 2 - idiagl
            if velha[idiagl][idiagc] == s:
                soma += 1
        if soma == 3:
            vitoria = "s"
            break
    return vitoria

def reiniciar():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vitoria
    velha = [[" "," "," "],[" "," "," "],[" "," "," "]]
    jogadas = 0
    quemJoga = 2
    maxJogadas = 9
    vitoria = "n"

jogarNovamente = input("Deseja jogar? (s/n): ").lower()

while jogarNovamente == "s":
    reiniciar() # Garante que o jogo sempre comece do zero
    while True:
        tela()
        jogadorJoga()
        vitoria = verificarVitoria()
        if vitoria != "n":
            break
        if jogadas == maxJogadas:
            break

        tela()
        cpuJoga()
        vitoria = verificarVitoria()
        if vitoria != "n":
            break
        if jogadas == maxJogadas:
            break

    tela() # Exibe a tela final
    if vitoria == "s":
        if quemJoga == 1: # Se quem jogou por último foi a CPU, o jogador ganhou
            print(Fore.GREEN + "Parabéns! Você venceu!" + Fore.RESET)
        else: # Se quem jogou por último foi o jogador, a CPU ganhou
            print(Fore.RED + "A CPU venceu!" + Fore.RESET)
    else:
        print(Fore.YELLOW + "Empate!" + Fore.RESET)

    jogarNovamente = input("Jogar novamente? (s/n): ").lower()

print("Fim de jogo!")
