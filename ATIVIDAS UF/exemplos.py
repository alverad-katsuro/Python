from math import log
def ef_cache():
    acerto = eval(input("Digite a quantidade de acertos: "))
    acessos = eval(input("Digite a quantidade de acessos: "))
    E = acerto / acessos
    return E


def bit_dados():
    cap = eval(input("Digite a capacidade da cache: "))
    byte = eval(input("Digite a quantidade de bits: "))
    cap_larg = cap * byte
    print(f"O total de bits de dados é {cap_larg} e possui {cap_larg.bit_length()} bits em seu comprimento")
    return cap, byte, cap_larg


def bit_tag(qt_blocos, qt_linhas):
    bits_tag = qt_blocos / qt_linhas
    print(f"A quantidade de bits na tag é {log(bits_tag,2)}")
    qt_bitsnas_linhas = qt_linhas * log(bits_tag,2)
    return qt_bitsnas_linhas


def dese_memodire(capacidade, largura_linhas, linhas):
    cap_bit = int(log(capacidade,2))
    larg_lin_bit = int(log(largura_linhas,2))
    lin_bit = int(log(linhas,2))
    print("{:-^33}".format(str(cap_bit) + " bits"))
    print("{}{: ^30}{}".format((cap_bit-lin_bit-larg_lin_bit),(lin_bit),(larg_lin_bit)))
    print("{:-^33}".format(''))
    return (cap_bit-lin_bit-larg_lin_bit), lin_bit, larg_lin_bit, cap_bit


def conv_pot(pot):
    if pot < 11:
        if pot == 10:
            pot0 = pot - 10
            letra = "Kbit"
        else:
            pot0 = pot
            letra = "bit"
    elif 10 < pot < 21:
        if pot == 20:
            pot0 = pot - 20
            letra = "Mbit"
        else:
            pot0 = pot - 10
            letra = "Kbit"
    elif 20 < pot < 31:
        if pot == 30:
            pot0 = pot - 30
            letra = "Gbit"
        else:
            pot0 = pot - 20
            letra = "Mbit"
    return pot0, letra


def exemplo5_1():
    print("Exemplo 5.1")
    print("Um determinado sistema de computação possui uma memória cache, MP e processador. Em operações normais, obtêm-se 96 acertos para cada 100 acessos do processador às memórias. Qual deve ser a eficiência do sistema cache/MP")
    E = ef_cache()
    print(f"A eficiencia é {E * 100}%")

def exemplo5_2():
    print("Cálculo da quantidade de bits necessários para uma determianda memória cache")
    print("Considere um sistema de computação com uma memória cache de 32KB de capacidade, constituida de linhas de linhas com 8 bytes de largura. A MP possui uma capacidade de 16MB.")
    cap_larg = bit_dados()
    blocos = eval(input("Digite a capacidade da MP: ")) / cap_larg[1]
    linhas = cap_larg[0] / cap_larg[1]
    tag_bit = bit_tag(blocos, linhas)
    pot = log(cap_larg[2]+tag_bit,2)
    pot_letra = conv_pot(pot)
    print(f"A quantidade de bits necessários é {round(2**pot_letra[0],0)} {pot_letra[1]}")

def exemplo5_3():
    print("Calcule o formato de endereço para memórias cache com mapeamento direto")
    print("Considere uma MP com 64MB de capacidade associada a uma memória cache que possui 2K linhas, cada uma com largura de 16 bytes. Determine o formato do endereço para ser interpretado pelo sistema de controle da cache.")
    capacidade = eval(input("Digite a capacidade da MP: "))
    largura_linhas = eval(input("Digite a largura da cache: "))
    linhas = eval(input("Digite a quantidade de linhas da cache: "))
    dese_memodire(capacidade,largura_linhas,linhas)

def exemplo5_4():
    print("Seja uma MP constituida de blocos com largura de 32 bytes, associada a uma cache com 128KB. Em dado instante o processador realiza um acesso, colocando o seguinte endereço 3FC92B6")
    binario = f"{0x3FC92B6:28b}"
    capacidade = eval(input("Digite a capacidade da MP: "))
    largura_linhas = eval(input("Digite a largura da cache: "))
    linhas = eval(input("Digite a capacidade do cache: ")) / largura_linhas
    x = dese_memodire(capacidade, largura_linhas, linhas)
    print("{:-^50}".format(str(x[3]) + " bits"))
    print("{}{: ^30}{}".format((binario[0:x[0]]), (binario[x[0]:x[0]+x[1]]), (binario[x[0]+x[1]:])))
    print("{:-^50}".format(''))


def exemplo5_5():
    print("Cálculo da quantidade de bits necessária para uma determinada memória cache.\nConsidere um sistema de computação com uma memória cache de 32KB de capacidade, constituida de linhas com 8 bytes de largura. A MP possui uma capacidade de 16MB")
    cap_larg = bit_dados()
    linhas =  cap_larg[0] / cap_larg[1]
    blocos = eval(input("Digite a capacidade da MP")) / cap_larg[1]
    bit_bloco_linha = linhas * log(blocos,2)
    pot = log(cap_larg[2] + bit_bloco_linha, 2)
    pot_letra = conv_pot(pot)
    print(f"A quantidade de bits necessários é {round(2 ** pot_letra[0],2)} {pot_letra[1]}")


def exemplo5_6():



def exemplo5_7():
    pass
def exemplo5_8():
    pass
def exemplo5_9():
    pass
def exemplo5_10():
    pass

exemplo5_1()