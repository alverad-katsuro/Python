from time import sleep
from random import choice

memoria = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0}
memoria_cache = {}
lista_keys = list(memoria.keys())

def leitura():
    endereco = input("Digite o endereço de 4 bits: ")
    if len(endereco) == 4:
        endereco = int(endereco, 2)
        if endereco in memoria_cache:
            print(f"\033[33mDado na memória cache\nO dado em {endereco:04b} é {memoria_cache[endereco]:08b}")
        else:
            print(f"\033[35mO dado em está na MP {endereco:04b} é {memoria[endereco]:08b}")
    else:
        print("\033[31mDigite um endereço valido")
        leitura()


def escrita():
    endereco = input("Digite o endereço de 4 bits: ")
    celula = input("Digite o valor da célula 8 bits: ")
    if len(endereco) == 4:
        endereco = int(endereco, 2)
        if len(celula) == 8:
            celula = int(celula)
            memoria[endereco] = celula
        else:
            print("\033[31Digite uma célula valida")
    else:
        print("\033[31Digite um endereço valido")
    memo_cache()


def memo_cache():
    global lista_keys
    par = {}
    impa = {}
    while (len(par) < 4) or (len(impa) < 4):
        escolha = choice(lista_keys)
        if (escolha % 2 == 0) and len(par) < 4:
            if escolha not in par:
                par.update({escolha:memoria[escolha]})
        else:
            if escolha not in impa and len(impa) < 4:
                impa.update({escolha:memoria[escolha]})
    memoria_cache.update(par)
    memoria_cache.update(impa)


def ler_tudo():
    print("{:-^30}".format("Memória Principal"))
    for k in range(len(memoria)):
        print(f"Endereço {k:04b} valor {memoria[k]:08b}")
    print("{:-^30}".format("Memória Cache"))
    for keys in memoria_cache.keys():
        bina = f'{keys:04b}'
        tag = bina[:3]
        conj = bina[3:4]
        print(f"Tag: {tag} Conjunto: {conj} Valor: {memoria_cache[keys]:08b}")
    sleep(5)


controle = "w"
memo_cache()
while (controle == "W") or (controle == "w") or (controle == "R") or (controle == "r") or (controle == "L") or (controle == "l"):
    controle = input("\033[34mDigite:\nW para escrever\nR para ler\nL para ler tudo\nQualquer tecla para parar\n")
    if (controle == "W") or (controle == "w"):
        escrita()
    elif (controle == "R") or (controle == "r"):
        leitura()
    elif (controle == "L") or (controle == "l"):
        ler_tudo()
    else:
        exit()
