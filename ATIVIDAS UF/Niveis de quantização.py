from time import sleep


#Quais bits estão em cada nivel#
def entrada():
    ent = input("\033[34mEntre com a quantidade de niveis\n")
    try:
        if isinstance(int(ent),int):
            if int(ent) >0:
                return int(ent)
            else:
                print("\033[34mVocê é besta?\nDigite um valor inteiro > 0\n")
                sleep(1.5)
                entrada()
    except ValueError:
        print("\033[34mVocê é besta?\nDigite um valor inteiro >0\n")
        sleep(1.5)
        entrada()

def bit_por_nivel(ent):
    n = 0
    lista_bits = []
    if ent % 2 != 0:
        ent += 1
    while 2**n != ent:
        n += 1
        bit = n
    intervalo = 2**bit
    print("\033[34mO intervalo de valores (números inteiros)"
          " que podem ser armazenados por uma 'palavra'"
          " de %a Bit é de %a informações diferentes" %(bit,intervalo))
    a = 0
    while a != 1 and a != 2:
        a = input("\033[34mVocê quer a lista de bits?\n1. Para sim\n2. Para não\n")
        try:
            if isinstance(int(a),int):
                a = int(a)
        except ValueError:
            print("\033[31;1mError 404")
            sleep(5)
            print("Digite 1 ou 2")
    for k in range(ent):
        lista_bits.append(int(format(k,'b')))

    if a == 1:
        print(lista_bits)
        return
    else:
        print("\033[34mQue pena")
        return

def chama_td():
    x = entrada()
    bit_por_nivel(x)

chama_td()