from time import sleep

memoria = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0}

def leitura():
    global memoria
    endereco = input("Digite o endereço de 4 bits: ")
    if len(endereco) == 4:
        endereco = int(endereco,2)
        print(f"O dado em {endereco} é {memoria[endereco]:08d}",)
    else:
        print("Digite um endereço valido")
        leitura()


def escrita():
    global memoria
    endereco = input("Digite o endereço de 4 bits: ")
    celula = input("Digite o valor da célula 8 bits: ")
    if len(endereco) == 4:
        endereco = int(endereco,2)
        if len(celula) == 8:
            celula = int(celula)
            memoria[endereco] = celula
        else:
            print("Digite uma célula valida")
    else:
        print("Digite um endereço valido")


def ler_tudo():
    global memoria
    inicio = 0
    while inicio <= 15:
        print(f"{memoria[inicio]:08d}")
        inicio += 1
    sleep(5)


controle = "w"
while (controle == "W") or (controle == "w") or (controle == "R") or (controle == "r") or (controle == "L") or (controle == "l"):
    controle = input("Digite:\nW para escrever\nR para ler\nL para ler tudo\nQualquer tecla para parar\n")
    if (controle == "W") or (controle == "w"):
        escrita()
    elif (controle == "R") or (controle == "r"):
        leitura()
    elif (controle == "L") or (controle == "l"):
        ler_tudo()
    else:
        exit()