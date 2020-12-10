import sys

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

ponto_usuario =0
ponto_computador =0
def partida():
    n = int(input("Escolha o número de peças inicais: "))
    m = int(input('Escolha o número maximo de peças a ser retirada por partida: '))
    if n and m < 0:
        print('Insira valores maiores que 0')
        partida()
    else:
        start(n, m)


def start(n, m):
    if n % (m + 1) != 0:
        print("Vou começar")
        ordem1(n,m)
    else:
        print('Você começa')
        ordem2(n,m)


def ordem1(n,m):
    while n>0:
        pc_ranger=computador_escolhe_jogada(n,m)
        n=n-pc_ranger
        if n==0:
            z=1
            print('Computador Ganhou')
            return z
        if n >0:
            m1=usuario_escolhe_jogada(n,m)
            n=n-m1
            if n==0:
                z=0
                print('Jogador ganhou!!')
                return z


def ordem2(n,m):
    while n>0:
        m1= usuario_escolhe_jogada(n, m)
        n=n-m1
        if n >0:
            pc_ranger= computador_escolhe_jogada(n, m)
            n=n-pc_ranger
            if n==0:
                z=1
                print('Computador Ganhou')
                return z
        else:
            print('Usuario Ganhou')
            z=0
            return z

def campeonato():
    global ponto_usuario
    global ponto_computador
    camp= ponto_usuario + ponto_computador
    while camp <3:
        z=partida()
        if z==0:
            ponto_usuario +=1
            print('Placar: Você %s X %s Computador'%(ponto_usuario,ponto_computador))
        else:
            ponto_computador +=1
            print('Placar: Você %s X %s Computador'%(ponto_usuario,ponto_computador))
        camp = ponto_usuario + ponto_computador
    if ponto_computador > ponto_usuario:
        print('Computador ganhou o Campeonato')
    else:
        print('Usuario Ganhou o Campeonato')



def computador_escolhe_jogada(n, m):
    for pc_range in reversed(range(1, m + 1)):
        if m>=n:
            pc_range=n
            n = n-pc_range
            print('O Computador retirou %d peça(s)' % pc_range)
            return pc_range
        elif n%(m+1) >0:
            pc_range = n%(m+1)
            n = n - pc_range
            print('O Computador retirou %d peça(s)' % pc_range)
            print("Sua vez")
            return pc_range
        else:
            n = n - pc_range
            if n > 0:
                print('O Computador retirou %d peça(s)' % pc_range)
                print("Sua vez")
                return pc_range
            else:
                computador_escolhe_jogada(n,m)


def usuario_escolhe_jogada(n: object, m: object) -> object:
    m1 = int(input("Escolha a quantida de peças a ser retirada"))
    while m1 <= 0 or m1 > m or m1 > n:
        print("Jogada invalida")
        m1 = int(input("Escolha a quantida de peças a ser retirada"))
    n = n - m1
    if n == 0:
        print('Você retirou %d peça(s)' % m1)
        return m1
    else:
        print('Você retirou %d peça(s)' % m1)
        return m1

main()