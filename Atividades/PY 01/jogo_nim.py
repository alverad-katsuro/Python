import random
import time
import sys


def main():
    ponto_j = 0
    ponto_pc = 0
    camp = 0
    game_start = int(input(
        "Bem-vindo ao jogo do NIM!\nEscolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))
    if game_start == 1:
        print('Você escolheu um jogo isolado')
        partida(ponto_pc, ponto_j,camp)
    elif game_start == 2:
        print('Voê selecionou um Campeonato!!')
        camp = 1
        campeonato(ponto_pc, ponto_j,camp)
    else:
        print('Digite a resposta corretamente')
        main()


def partida(ponto_pc, ponto_j,camp):
    n = int(input("Escolha o número de peças inicais: "))
    m = int(input('Escolha o número maximo de peças a ser retirada por partida: '))
    if n and m < 0:
        print('Insira valores maiores que 0')
        partida()
    else:
        start(n, m, ponto_pc, ponto_j,camp)


def start(n, m, ponto_pc, ponto_j,camp):
    if n % (m + 1) != 0:
        print("Vou começar")
        game_1(n, m, ponto_pc, ponto_j,camp)
    else:
        print('Você começa')
        game_2(n, m, ponto_pc, ponto_j,camp)


def computador_escolhe_jogada(n, m, ponto_pc, ponto_j,camp):
    for pc_range in reversed(range(1, m + 1)):
        n = n - pc_range
        if n == 0 or n < 0:
            print("Eu ganhei hahhahahaha")
            if camp == 1:
                ponto_pc = ponto_pc + 1
                print("Placar: Você %d X %d Computador" %(ponto_j,ponto_pc))
                campeonato(ponto_pc,ponto_j,camp)
            else:
                sys.exit()
        elif n % (m + 1) != 0:
            print("Restam %d peças" % n)
            print("Sua vez")
            usuario_escolhe_jogada(n, m, ponto_pc, ponto_j,camp)


def game_1(n, m, ponto_pc, ponto_j,camp):
    while n > 0:
        computador_escolhe_jogada(n, m, ponto_pc, ponto_j,camp)


def game_2(n, m, ponto_pc, ponto_j,camp):
    while n > 0:
        usuario_escolhe_jogada(n, m, ponto_pc, ponto_j,camp)


def game_solo():
    start()
    jogar_dnv()


def campeonato(ponto_pc, ponto_j, camp):
    fim = ponto_j + ponto_pc
    while fim < 3:
        partida(ponto_pc, ponto_j,camp)
    if ponto_j > ponto_pc:
        print('Parabens você ganhou')
        sys.exit()
    else:
        print('Choraaaa você perdeu')
        sys.exit()


def usuario_escolhe_jogada(n, m, ponto_pc, ponto_j,camp):
    print("O número de peças é %d" % n)
    m1 = int(input("Escolha a quantida de peças a ser retirada"))
    if m1 == 0 or m1 > m:
        print("Escolha um número entr 0 e %d" % m)
        usuario_escolhe_jogada(n, m, ponto_pc, ponto_j,camp)
    n = n - m1
    if n == 0 or n < 0:
        print('Você ganhou :/')
        if camp == 1:
            ponto_j = ponto_j + 1
            print("Placar: Você %d X %d Computador" %(ponto_j,ponto_pc))
            campeonato(ponto_pc,ponto_j,camp)
        else:
            sys.exit()
    else:
        print('O número de peças agora é igual a %d' % n)
        computador_escolhe_jogada(n, m, ponto_pc, ponto_j,camp)


def jogar_dnv():
    novamente = input("Você que jogar novamente?\nDigite 1 pra sim e 2 pra não")
    if novamente == 1:
        print("uhuuuu")
        main()
    else:
        print("Até mais então")
        sys.exit()

main()

def computador_escolhe_jogada(n, m):
    for pc_range in reversed(range(1, m + 1)):
        n = n - pc_range
        if n == 0 or n < 0:
            print("Eu ganhei hahhahahaha")
            sys.exit()
        elif n % (m + 1) != 0:
            print("Restam %d peças" % n)
            print("Sua vez")

def usuario_escolhe_jogada(n, m):
    print("O número de peças é %d" % n)
    m1 = int(input("Escolha a quantida de peças a ser retirada"))
    if m1 == 0 or m1 > m:
        print("Escolha um número entr 0 e %d" % m)
        usuario_escolhe_jogada1(n, m)
    n = n - m1
    if n == 0 or n < 0:
        print('Você ganhou :/')
        sys.exit()
    else:
        print('O número de peças agora é igual a %d' % n)
        computador_escolhe_jogada1(n, m)