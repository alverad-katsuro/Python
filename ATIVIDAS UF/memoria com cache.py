from random import choice


memoria = {0: 1, 1: 12, 2: 4, 3: 14, 4: 4, 5: 12, 6: 8, 7: 6, 8: 10, 9: 14, 10: 0, 11: 0, 12: 2, 13: 179, 14: 1, 15: 163}
memoria_cache = {0: {}, 1: {}}
lista_keys = list(memoria.keys())


class Process:
    def __init__(self):
        self.processador = True
        self.ci = 0

    def cpu(self):
        global r0
        while self.ci != -1:
            rem = self.ci
            rdm = leitura(rem, self.processador)
            ri = rdm
            if ri[0] == 0:  # Break
                self.ci = -1
                break
            elif ri[0] == 1:  # Load
                rdm = leitura(ri[1], self.processador)
                r0 = int(f'{rdm[0]:08b}' + f'{rdm[1]:08b}', 2)
            elif ri[0] == 2:  # STORE?
                pass
            elif ri[0] == 3:  # Soma
                rdm = leitura(ri[1], self.processador)
                r0 = r0 + int(f'{rdm[0]:08b}' + f'{rdm[1]:08b}', 2)
            elif ri[0] == 4:  # Subtracao
                rdm = leitura(ri[1], self.processador)
                r0 = r0 - int((f'{rdm[0]:08b}' + f'{rdm[1]:08b}'), 2)
            elif ri[0] == 5:  # JZ
                if r0 == 0:
                    self.ci = ri[1]
            elif ri[0] == 6:  # JP
                if r0 > 0:
                    self.ci = ri[1]
            elif ri[0] == 7:  # JN
                if r0 < 0:
                    self.ci = ri[1]
            elif ri[0] == 8:  # JUMP
                self.ci = ri[1]
            elif ri[0] == 9:  # GET
                pass
            elif ri[0] == 10:  # PRINT
                pass
            else:
                print("Algo deu erro")
                break
            print(self.ci)
            self.ci += 2


def mani_end(endereco):
    tag = int(endereco[0:2], 2)
    conj = int(endereco[2], 2)
    dado = int(endereco[3], 2)
    return tag, conj, dado


def leitura(endereco=0, processador=False):
    if not processador:
        endereco = input("Digite o endereço de 4 bits: ")
        if len(endereco) == 4:
            tag, conj, dado = mani_end(endereco)
            if tag in memoria_cache[conj]:
                print("Esta na Memória Cache")
                print(
                    f"\033[33mTag: {tag:02b} Conjunto: {conj} Dado {dado} Valor: {memoria_cache[conj][tag][dado]:08b}")
            else:
                print(f"\033[35mO dado em está na MP {endereco:04b} é {memoria[endereco]:08b}")
        else:
            print("\033[31mDigite um endereço valido")
            leitura()
    else:
        tag, conj, dado = mani_end(f'{endereco:04b}')
        if tag in memoria_cache[conj]:
            return memoria_cache[conj][tag][0], memoria_cache[conj][tag][1]
        else:
            escrita(endereco, processador)
            return memoria_cache[conj][tag][0], memoria_cache[conj][tag][1]


def mani_escri(endereco, celula):
    endereco = int(endereco, 2)
    celula = int(celula, 2)
    b_end = f'{endereco:04b}'
    tag = int(b_end[0:2], 2)
    conj = int(b_end[2], 2)
    dado = int(b_end[3], 2)
    memoria[endereco] = -1
    if tag not in memoria_cache[conj]:
        del (memoria_cache[conj][choice(list(memoria_cache[conj].keys()))])
        memoria_cache[conj].update({tag: {}})
        memoria_cache[conj][tag].update({dado: celula})
        if dado == 0:
            memoria_cache[conj][tag][1] = memoria[endereco + 1]
        else:
            memoria_cache[conj][tag][0] = memoria[endereco - 1]
    else:
        memoria_cache[conj][tag][dado] = celula
    memoria[endereco] = celula


def escrita(endereco=0, processador=False):
    if not processador:
        endereco = input("Digite o endereço de 4 bits: ")
        celula = input("Digite o valor da célula 8 bits: ")
        if len(endereco) == 4:
            if len(celula) == 8:
                mani_escri(endereco, celula)
            else:
                print("\033[31Digite uma célula valida")
                escrita()
        else:
            print("\033[31Digite um endereço valido")
            escrita()
    else:
        memo_cache_escrita(endereco)


def memo_cache_escrita(endereco):
    if endereco in range(0, len(memoria), 4):
            memoria_cache[0].update({endereco >> 2: {}})
            memoria_cache[0][endereco >> 2].update({1: memoria[endereco + 1]})
            memoria_cache[0][endereco >> 2].update({0: memoria[endereco]})
    elif endereco in range(2, len(memoria), 4):
            memoria_cache[1].update({endereco >> 2: {}})
            memoria_cache[1][endereco >> 2].update({1: memoria[endereco + 1]})
            memoria_cache[1][endereco >> 2].update({0: memoria[endereco]})


def memo_cache_random():
    global memoria_cache
    for conju in range(len(memoria_cache)):
        for r in range(len(memoria_cache)):
            escolha = choice(lista_keys)
            if escolha in range(0, len(memoria), 4):
                if escolha >> 2 not in memoria_cache[0] and len(memoria_cache[0]) < 2:
                    memoria_cache[0].update({escolha >> 2: {}})
                    memoria_cache[0][escolha >> 2].update({1: memoria[escolha + 1]})
                    memoria_cache[0][escolha >> 2].update({0: memoria[escolha]})
            elif escolha in range(2, len(memoria), 4) and len(memoria_cache[1]) < 2:
                if escolha not in memoria_cache[1]:
                    memoria_cache[1].update({escolha >> 2: {}})
                    memoria_cache[1][escolha >> 2].update({1: memoria[escolha + 1]})
                    memoria_cache[1][escolha >> 2].update({0: memoria[escolha]})
    if len(memoria_cache[0]) < 2 or len(memoria_cache[1]) < 2:
        memo_cache_random()


def ler_tudo():
    print("\033[33m{:-^30}".format("Memória Cache"))
    for cj in range(len(memoria_cache)):
        for tag in memoria_cache[cj].keys():
            print(f"\033[33mTag: {tag:02b} Conjunto: {cj} Dado 0 Valor: {memoria_cache[cj][tag][0]:08b}", end=" ")
            print(f"Dado 1 Valor: {memoria_cache[cj][tag][1]:08b}")
    print("\033[35m{:-^30}".format("Memória Principal"))
    for k in range(len(memoria)):
        print(f"\033[35mEndereço {k:04b} valor {memoria[k]:08b}")

memo_cache_random()
controle = "w"
while controle in "WwRrLlPp":
    processador = False
    controle = input("\033[34mDigite:\nW - Write\nR - READER\nL - READ ALL\nP para executar instruções\nQualquer tecla para parar\n")
    if (controle == "W") or (controle == "w"):
        escrita()
    elif (controle == "R") or (controle == "r"):
        leitura()
    elif (controle == "L") or (controle == "l"):
        ler_tudo()
    elif (controle == "P") or (controle == "p"):
        a = Process()
        a.cpu()
    else:
        exit()
