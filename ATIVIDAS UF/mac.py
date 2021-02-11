from random import choice
from random import randrange


print("Projeto de Memória")

# definir que todos os 16 endereços começarão sem nenhum dado gravado e uma célula temporária

mp = {0: "00000000", 1: "00000000", 2: "00000000", 3: "00000000", 4: "00000000", 5: "00000000", 6: "00000000", 7: "00000000", 8: "00000000", 9: "00000000", 10: "00000000", 11: "00000000", 12: "00000000", 13: "00000000", 14: "00000000", 15: "00000000"}

mc = {0: "00000000", 1: "00000000", 2: "00000000", 3: "00000000", 4: "00000000", 5: "00000000", 6: "00000000", 7: "00000000"}

mc_end = {0: "0000", 1: "1000", 2: "0010", 3: "0110"}


def escrita_mc(end, dado):
    end_dec = int(end, 2)
    x = end
    if end_dec % 2 != 0:
        x = int(end, 2) - 1
        x = f'{x:04b}'
    if end in mc_end.values() or x in mc_end.values():
        if end == mc_end[0]:
            if end[3] == '0':
                mc[0] = dado
            else:
                mc[1] = dado
        if end == mc_end[1]:
            if end[3] == '0':
                mc[2] = dado
            else:
                mc[3] = dado
        if end == mc_end[2]:
            if end[3] == '0':
                mc[4] = dado
            else:
                mc[5] = dado
        if end == mc_end[3]:
            if end[3] == '0':
                mc[6] = dado
            else:
                mc[7] = dado
    else:
        if end[3] == "0":
            dado0 = dado
            dado1 = mp[end_dec + 1]
        else:
            dado1 = dado
            dado0 = mp[end_dec - 1]
        if end[2] == "0":
            x = randrange(1)
            if x == 0:
                mc_end[0] = end
                if end[3] == '0':
                    mc[0] = dado0
                    mc[1] = dado1
                else:
                    mc[1] = dado1
                    mc[0] = dado0
            else:
                mc_end[1] = end
                if end[3] == '0':
                    mc[2] = dado0
                    mc[3] = dado1
                else:
                    mc[3] = dado1
                    mc[2] = dado0
        else:
            x = randrange(1)
            if x == 0:
                mc_end[2] = end
                if end[3] == '0':
                    mc[4] = dado0
                    mc[5] = dado1
                else:
                    mc[5] = dado1
                    mc[4] = dado0
            else:
                mc_end[3] = end
                if end[3] == '0':
                    mc[6] = dado0
                    mc[7] = dado1
                else:
                    mc[7] = dado1
                    mc[8] = dado0

# Primeiramente, configurar a opção de leitura da memória

while True:
    a = input('''\nPressione W para escrita, R para leitura, ou L para apresentação total das 16 células de 8 bits. E posteriormente, qualquer tecla para parar.
(Cada célula tem relação com um número de endereço para ser localizada): ''')
    if a == "L":
        print('''Todos os endereços da memória principal: ''' +
              '\nTAG: ' +mc_end[0][0:2] + ' Conjunto: 0' + " Dado 0: " + mc[0] + " Dado 1: " + mc[1] +
              '\nTAG: ' +mc_end[1][0:2] + ' Conjunto: 0' + " Dado 0: " + mc[2] + " Dado 1: " + mc[3] +
              '\nTAG: ' +mc_end[2][0:2] + ' Conjunto: 1' + " Dado 0: " + mc[4] + " Dado 1: " + mc[5] +
              '\nTAG: ' +mc_end[3][0:2] + ' Conjunto: 1' + " Dado 0: " + mc[6] + " Dado 1: " + mc[7])
        print("Todos os endereços da memória principal")
        for k in range(16):
            print(mp[k])
    # inserir a instrução de escrita, bem como as correções, caso algo não esteja de acordo com o código

    if a == "W":
        saida = input("Digite o endereço de 4 bits: ")
        if saida == "0000":
            non = input("Digite um dado de 8 bits: ")
            if len(non) > 8 or len(non) < 8:
                print("Endereço inválido, por favor respeite a condição de 8 bits.")
            else:
                escrita_mc(saida, non)
                mp[0] = non
        if saida == "0001":
            non = input("Digite um dado de 8 bits: ")
            if len(non) > 8 or len(non) < 8:
                print("Endereço inválido, por favor respeite a condição de 8 bits.")
            else:
                escrita_mc(saida, non)
                mp[1] = non
        if saida == "0010":
            non = input("Digite um dado de 8 bits: ")
            if len(non) > 8 or len(non) < 8:
                print("Endereço inválido, por favor respeite a condição de 8 bits.")
            else:
                escrita_mc(saida, non)
                mp[2] = non
        if saida == "0011":
            non = input("Digite um dado de 8 bits: ")
            if len(non) > 8 or len(non) < 8:
                print("Endereço inválido, por favor respeite a condição de 8 bits.")
            else:
                escrita_mc(saida, non)
                mp[3] = non
        if saida == "0100":
            non = input("Digite um dado de 8 bits: ")
            if len(non) > 8 or len(non) < 8:
                print("Endereço inválido, por favor respeite a condição de 8 bits.")
            else:
                escrita_mc(saida, non)
                mp[4] = non
        if saida == "0101":
            non = input("Digite um dado de 8 bits: ")
            if len(non) > 8 or len(non) < 8:
                print("Endereço inválido, por favor respeite a condição de 8 bits.")
            else:
                escrita_mc(saida, non)
                mp[5] = non
        if saida == "0110":
            non = input("Digite um dado de 8 bits: ")
            if len(non) > 8 or len(non) < 8:
                print("Endereço inválido, por favor respeite a condição de 8 bits.")
            else:
                escrita_mc(saida, non)
                mp[6] = non
        if saida == "0111":
            non = input("Digite um dado de 8 bits: ")
            if len(non) > 8 or len(non) < 8:
                print("Endereço inválido, por favor respeite a condição de 8 bits.")
            else:
                escrita_mc(saida, non)
                mp[7] = non
        if saida == "1000":
            non = input("Digite um dado de 8 bits: ")
            if len(non) > 8 or len(non) < 8:
                print("Endereço inválido, por favor respeite a condição de 8 bits.")
            else:
                escrita_mc(saida, non)
                mp[8] = non
        if saida == "1001":
            non = input("Digite um dado de 8 bits: ")
            if len(non) > 8 or len(non) < 8:
                print("Endereço inválido, por favor respeite a condição de 8 bits.")
            else:
                escrita_mc(saida, non)
                mp[9] = non
        if saida == "1010":
            non = input("Digite um dado de 8 bits: ")
            if len(non) > 8 or len(non) < 8:
                print("Endereço inválido, por favor respeite a condição de 8 bits.")
            else:
                escrita_mc(saida, non)
                mp[10] = non
        if saida == "1011":
            non = input("Digite um dado de 8 bits: ")
            if len(non) > 8 or len(non) < 8:
                print("Endereço inválido, por favor respeite a condição de 8 bits.")
            else:
                escrita_mc(saida, non)
                mp[11] = non
        if saida == "1100":
            non = input("Digite um dado de 8 bits: ")
            if len(non) > 8 or len(non) < 8:
                print("Endereço inválido, por favor respeite a condição de 8 bits.")
            else:
                escrita_mc(saida, non)
                mp[12] = non
        if saida == "1101":
            non = input("Digite um dado de 8 bits: ")
            if len(non) > 8 or len(non) < 8:
                print("Endereço inválido, por favor respeite a condição de 8 bits.")
            else:
                escrita_mc(saida, non)
                mp[13] = non
        if saida == "1110":
            non = input("Digite um dado de 8 bits: ")
            if len(non) > 8 or len(non) < 8:
                print("Endereço inválido, por favor respeite a condição de 8 bits.")
            else:
                escrita_mc(saida, non)
                mp[14] = non
        if saida == "1111":
            non = input("Digite um dado de 8 bits: ")
            if len(non) > 8 or len(non) < 8:
                print("Endereço inválido, por favor respeite a condição de 8 bits.")
            else:
                escrita_mc(saida, non)
                mp[15] = non



    # Já neste bloco, a operação de leitura será disponibilizada

    if a == "R":
        end = input("Digite um dos endereço de 4 bits: ")
        if end in mc_end.values():
            print("O endereço está na MC")
            print(mp[int(end, 2)])
        else:
            print("O enreço está na MP")
            print(mp[int(end, 2)])


