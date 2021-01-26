from random import choice

memoria = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0}
memoria_cache = {0: {}, 1: {}}
lista_keys = list(memoria.keys())


def leitura():
    endereco = input("Digite o endereço de 4 bits: ")
    if len(endereco) == 4:
        endereco = int(endereco, 2)
        b_end = f'{endereco:04b}'
        tag = int(b_end[0:2], 2)
        conj = int(b_end[2], 2)
        dado = int(b_end[3], 2)
        if tag in memoria_cache[conj]:
            print("Esta na Memória Cache")
            print(f"\033[33mTag: {tag:02b} Conjunto: {conj} Dado {dado} Valor: {memoria_cache[conj][tag][dado]:08b}")
        else:
            print(f"\033[35mO dado em está na MP {endereco:04b} é {memoria[endereco]:08b}")
    else:
        print("\033[31mDigite um endereço valido")
        leitura()


def escrita():
    endereco = input("Digite o endereço de 4 bits: ")
    celula = input("Digite o valor da célula 8 bits: ")
    if len(endereco) == 4:
        if len(celula) == 8:
            endereco = int(endereco, 2)
            celulad = int(celula, 2)
            b_end = f'{endereco:04b}'
            tag = int(b_end[0:2], 2)
            conj = int(b_end[2], 2)
            dado = int(b_end[3], 2)
            memoria[endereco] = -1
            if tag not in memoria_cache[conj]:
                del(memoria_cache[conj][choice(list(memoria_cache[conj].keys()))])
                memoria_cache[conj].update({tag: {}})
                memoria_cache[conj][tag].update({dado: celulad})
                if dado == 0:
                    memoria_cache[conj][tag][1] = memoria[endereco + 1]
                else:
                    memoria_cache[conj][tag][0] = memoria[endereco - 1]
            else:
                memoria_cache[conj][tag][dado] = celulad
            memoria[endereco] = celulad
        else:
            print("\033[31Digite uma célula valida")
    else:
        print("\033[31Digite um endereço valido")


def memo_cache():
    global memoria_cache
    for conju in range(len(memoria_cache)):
        for r in range(len(memoria_cache)):
            escolha = choice(lista_keys)
            if escolha in range(0, len(memoria), 4):
                if escolha >> 2 not in memoria_cache[0] and len(memoria_cache[0]) < 2:
                    memoria_cache[0].update({escolha >> 2: {}})
                    memoria_cache[0][escolha >> 2].update({1: memoria[escolha+1]})
                    memoria_cache[0][escolha >> 2].update({0: memoria[escolha+1]})
            elif escolha in range(2, len(memoria), 4) and len(memoria_cache[1]) < 2:
                if escolha not in memoria_cache[1]:
                    memoria_cache[1].update({escolha >> 2: {}})
                    memoria_cache[1][escolha >> 2].update({1: memoria[escolha + 1]})
                    memoria_cache[1][escolha >> 2].update({0: memoria[escolha + 1]})
    if len(memoria_cache[0]) < 2 or len(memoria_cache[1]) < 2:
        memo_cache()


def ler_tudo():
    print("\033[33m{:-^30}".format("Memória Cache"))
    for cj in range(len(memoria_cache)):
        for tag in memoria_cache[cj].keys():
            print(f"\033[33mTag: {tag:02b} Conjunto: {cj} Dado 0 Valor: {memoria_cache[cj][tag][0]:08b}", end=" ")
            print(f"Dado 1 Valor: {memoria_cache[cj][tag][1]:08b}")
    print("\033[35m{:-^30}".format("Memória Principal"))
    for k in range(len(memoria)):
        print(f"\033[35mEndereço {k:04b} valor {memoria[k]:08b}")


controle = "w"
memo_cache()
while controle in "WwRrLl":
    controle = input("\033[34mDigite:\nW para escrever\nR para ler\nL para ler tudo\nQualquer tecla para parar\n")
    if (controle == "W") or (controle == "w"):
        escrita()
    elif (controle == "R") or (controle == "r"):
        leitura()
    elif (controle == "L") or (controle == "l"):
        ler_tudo()
    else:
        exit()
