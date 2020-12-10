def main():
    bina1, bina2 = entrada()
    if bina1 == bina2:
        print("\033[34mO binario resultante é", 0)
    elif all(bina2[k] == '0' for k in range(len(bina2))):
        print("Digite um valor diferente de 0")
        main()
    else:
        bina2 = inversor(bina1, bina2)
        resultado = soma(bina1, bina2)
        print("\033[34mO binario resultante é", resultado)


def entrada():
    string = input("\033[34mDigite a equação na ordem BIN - BIN\n")
    string_permitida = "10- "
    lista1 = list(string)
    bina1 = []
    bina2 = []
    try:
        for i in range(len(lista1)):
            if not lista1[i] in string_permitida:
                print("\033[31mDigite um Binario certo na ordem certa")
                entrada()
    finally:
        menos = lista1.index("-")
        espaco = lista1.count(" ")
        for k in range(espaco):
            lista1.remove(" ")
        lista1.remove("-")
        for i in range(0, menos):
            bina1.append(lista1[i])
        for k in range(menos, len(lista1)):
            bina2.append(lista1[k])
        return bina1, bina2


def inversor(bina1, bina2: list):
    inversa = []
    while len(bina1)%4 != 0:
        bina2.insert(0,"0")
        if len(bina1) == len(bina2):
            break
    for i in range(len(bina2)):
        if int(bina2[i]) == 1:
            inversa.append("0")
        else:
            inversa.append("1")
    k = len(inversa) - 1
    if inversa[k] == "0":
        inversa[k] = "1"
    else:
        c = 1
        while c > 0:
            for j in reversed(range(len(inversa))):
                if inversa[j] == "1":
                    inversa[j] = "0"
                    if inversa[j-1] == "0":
                        inversa[j-1] = "1"
                        c = 0
                        break
    return inversa


def soma(bina1, bina2):
    sobra = 0
    bina1.insert(0, "0")
    bina2.insert(0, "0")
    if len(bina1) > len(bina2):
        k = len(bina1)-len(bina2)
        while k > 0:
            bina2.insert(0,"0")
            k -= 1
    else:
        k = len(bina2) - len(bina1)
        while k > 0:
            bina1.insert(0, "0")
            k -= 1
    bina_resultado = ""
    print(bina1,bina2)
    for j in reversed(range(len(bina1))):
        if bina1[j] == bina2[j] == "1":
            if sobra == 1:
                bina_resultado += "1"
            else:
                bina_resultado += "0"
                sobra = 1
        elif bina1[j] == "1" and bina2[j] == "0":
            if sobra == 1:
                bina_resultado += "0"
            else:
                bina_resultado += "1"
        elif bina1[j] == "0" and bina2[j] == "1":
            if sobra == 1:
                bina_resultado += "0"
            else:
                bina_resultado += "1"
        else:
            if sobra == 1:
                bina_resultado += "1"
                sobra = 0
            else:
                bina_resultado += "0"
    bina_resultado = bina_resultado.removesuffix("1")
    bina_resultado = bina_resultado[::-1]
    print(int(bina_resultado))
    return int(bina_resultado)


main()