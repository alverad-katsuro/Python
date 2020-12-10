import random
import time
import sys

import sys
def computador_escolhe_jogada(n, m):
    for pc_range in reversed(range(1, m + 1)):
        if m>=n:
            k=n
            n=n-n
            print('O Computador retirou %d peça(s)' % k)
            print("Eu ganhei hahhahahaha")
            return k
            sys.exit()
        elif n%(m+1) >0:
            pc_range = n%(m+1)
            n = n - pc_range
            print('O Computador retirou %d peça(s)' % pc_range)
            print("Restam %d peças" % n)
            print("Sua vez")
            return pc_range
            sys.exit()
        else:
            n = n - pc_range
            if n == 0:
                print('O Computador retirou %d peça(s)' % pc_range)
                print("Eu ganhei hahhahahaha")
                return pc_range
                sys.exit()
            elif n > 0:
                print('O Computador retirou %d peça(s)' % pc_range)
                print("Restam %d peças" % n)
                print("Sua vez")
                return pc_range
                sys.exit()
            else:
                computador_escolhe_jogada(n,m)

def usuario_escolhe_jogada(n: object, m: object) -> object:
    m1 = int(input("Escolha a quantida de peças a ser retirada: "))
    while m1 == 0 or m1 > m or m1 > n:
        print("Jogada invalida")
        m1 = int(input("Escolha a quantida de peças a ser retirada: "))
    n = n - m1
    if n == 0:
        print('Você retirou %d peça(s)' % m1)
        print('Você ganhou :/')
        return m1
    else:
        print('Você retirou %d peça(s)' % m1)
        print("Sobraram %d peça(s)"%n)
        return m1
####

def partida():
    n = int(input("Escolha o número de peças inicais: "))
    m = int(input('Escolha o número maximo de peças a ser retirada por partida: '))
    if n and m < 0:
        print('Insira valores maiores que 0')
        partida()
    else:
        start(n, m)

def main():
    game_start = int(input("Bem-vindo ao jogo do NIM!\nEscolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))
    if game_start == 1:
        print('Você escolheu um jogo isolado')
        partida()
    elif game_start == 2:
        print('Voê selecionou um Campeonato!!')
        campeonato()
    else:
        print('Digite a resposta corretamente')
        main()

def start(n, m):
    if n % (m + 1) != 0:
        print("Vou começar")
        while n > 0:
            computador_escolhe_jogada1(n, m)
    else:
        print('Você começa')
        while n > 0:
            usuario_escolhe_jogada1(n, m)


def computador_escolhe_jogada1(n, m):
    for pc_range in reversed(range(1, m + 1)):
        if m >= n:
            k = n
            n = n - n
            print('O Computador retirou %d peça(s)' % k)
            print("Eu ganhei hahhahahaha")
            sys.exit()
        elif n % (m + 1) > 0:
            pc_range = n % (m + 1)
            n = n - pc_range
            print('O Computador retirou %d peça(s)' % pc_range)
            print("Sua vez")
            usuario_escolhe_jogada1(n,m)
        else:
            n = n - pc_range
            if n == 0:
                print('O Computador retirou %d peça(s)' % pc_range)
                print("Eu ganhei hahhahahaha")
                sys.exit()
            elif n > 0:
                print('O Computador retirou %d peça(s)' % pc_range)
                print("Restam %d peças" % n)
                print("Sua vez")
                usuario_escolhe_jogada1(n,m)
            else:
                computador_escolhe_jogada(n, m)



def usuario_escolhe_jogada1(n, m):
    m1 = int(input("Escolha a quantida de peças a ser retirada: "))
    while m1 == 0 or m1 > m or m1 > n:
        print("Jogada invalida")
        m1 = int(input("Escolha a quantida de peças a ser retirada: "))
    n = n - m1
    if n == 0:
        print('Você retirou %d peça(s)' % m1)
        print('Você ganhou :/')
    else:
        print('Você retirou %d peça(s)' % m1)
        computador_escolhe_jogada1(n,m)

def pro_campeonato(ponto_pc,ponto_j,camp):
    fim = ponto_pc+ponto_j
    while fim <3:
        partida_camp(ponto_j, ponto_pc, camp)
    sys.exit()

def campeonato():
    ponto_j = 0
    ponto_pc = 0
    camp = 1
    pro_campeonato(ponto_pc,ponto_j,camp)




def partida_camp(ponto_j, ponto_pc,camp):
    n = int(input("Escolha o número de peças inicais: "))
    m = int(input('Escolha o número maximo de peças a ser retirada por partida: '))
    if n and m < 0:
        print('Insira valores maiores que 0')
        partida_camp(n, m,ponto_pc,ponto_j,camp)
    else:
        start_camp(n, m,ponto_pc,ponto_j,camp)

def start_camp(n, m,ponto_pc,ponto_j,camp):
    if n % (m + 1) != 0:
        print("Vou começar")
        while n > 0:
            camp_computador_escolhe_jogada1(n, m,ponto_pc,ponto_j,camp)
    else:
        print('Você começa')
        while n > 0:
            camp_usuario_escolhe_jogada1(n, m,ponto_pc,ponto_j,camp)

def camp_usuario_escolhe_jogada1(n, m,ponto_pc,ponto_j,camp):
    print("O número de peças é %d" % n)
    m1 = int(input("Escolha a quantida de peças a ser retirada"))
    if m1 == 0 or m1 > m:
        print("Escolha um número entr 0 e %d" % m)
        camp_usuario_escolhe_jogada1(n, m, ponto_pc, ponto_j, camp)
    n = n - m1
    if n == 0 or n < 0:
        print('Você ganhou :/')
        if camp == 1:
            ponto_j = ponto_j + 1
            print("Placar: Você %d X %d Computador" % (ponto_j, ponto_pc))
            pro_campeonato(ponto_pc, ponto_j,camp)
        else:
            sys.exit()
    elif n % (m + 1) != 0:
        print("Restam %d peças" % n)
        print("Sua vez")
        camp_computador_escolhe_jogada1(n, m, ponto_pc, ponto_j,camp)

def camp_computador_escolhe_jogada1(n, m,ponto_pc,ponto_j,camp):
    for pc_range in reversed(range(1, m + 1)):
        n = n - pc_range
        if n == 0 or n < 0:
            print("Eu ganhei hahhahahaha")
            if camp == 1:
                ponto_pc = ponto_pc + 1
                print("Placar: Você %d X %d Computador" % (ponto_j, ponto_pc))
                pro_campeonato(ponto_pc, ponto_j,camp)
            else:
                sys.exit()
        elif n % (m + 1) != 0:
            print("Restam %d peças" % n)
            print("Sua vez")
            camp_usuario_escolhe_jogada1(n, m, ponto_pc, ponto_j, camp)

partida()