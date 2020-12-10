from time import sleep
import sys

def entrada():
    c = 0
    while not 0 < c < 13:
        try:
            c = input("\033[34mDigite\n"
                      "1. Para conversor Decimal---Binario\n"
                      "2. Para conversor Decimal---Hexadecimal\n"
                      "3. Para conversor Decimal---Octadecimal\n"
                      "4. Para conversor Binario---Decimal\n"
                      "5. Para conversor Binario---Hexadecimal\n"
                      "6. Para conversor Binario---Octadecimal\n"
                      "7. Para conversor Hexadecimal---Binario\n"
                      "8. Para conversor Hexadecimal---Decimal\n"
                      "9. Para conversor Hexadecimal---Octagonal\n"
                      "10. Para conversor Octagonal---Hexadecimal\n"
                      "11. Para conversor Octagonal---Decimal\n"
                      "12. Para conversor Octagonal---Binario\n"
                      "")
            if isinstance(int(c), int):
                c = int(c)
                try:
                    if c == 1:
                        try:
                            bina = chama_dec_bin()
                            print("O valor do binário é", bina)
                        except ValueError:
                            print("\033[31mDigita o decimal certo lek")
                            sleep(1.5)
                            chama_dec_bin()
                        break
                    elif c == 4:
                        try:
                            dec = binarios()
                            print("O valor do binario em decimais vale:", dec)
                        except ValueError:
                            print("\033[31mDigita o binario certo lek")
                            sleep(1.5)
                            binarios()
                        break
                    elif c == 5:
                        try:
                            hexa = chama_bin_hex()
                            print("O valor do hexadecimal é", hexa)
                        except ValueError:
                            print("\033[31mDigite o binario certo lek")
                            sleep(1.5)
                            chama_bin_hex()
                        break
                    elif c == 6:
                        try:
                            octa = chama_bin_oct()
                            print("O valor do octadecimal é:", octa)
                        except ValueError:
                            print("\033[31mDigita o binario certo lek")
                            sleep(1.5)
                            chama_bin_oct()
                        break
                    elif c == 2:
                        try:
                            hexa = chama_dec_hex()
                            print("O valor do hexadecimal é", hexa)
                        except ValueError:
                            print("\033[31mDigita o decimal certo lek")
                            sleep(1.5)
                            chama_dec_hex()
                        break
                    elif c == 3:
                        try:
                            octa = chama_dec_oct()
                            print("O valor do octadecimal é", octa)
                        except ValueError:
                            print("\033[31mDigita o decimal certo lek")
                            sleep(1.5)
                            chama_dec_oct()
                        break
                    elif c == 7:
                        try:
                            bina = chama_hex_bin()
                            print("O valor do binario é", bina)
                        except ValueError:
                            print("\033[31mDigita o Hexadecimal certo lek")
                            sleep(1.5)
                            chama_hex_bin()
                        break
                    elif c == 8:
                        try:
                            deci = chama_hex_dec()
                            print("O valor do decimal é", deci)
                        except ValueError:
                            print("\033[31mDigita o Hexadecimal certo lek")
                            sleep(1.5)
                            chama_hex_dec()
                        break
                    elif c == 9:
                        try:
                            octa = chama_hex_oct()
                            print("O valor do octadecimal é", octa)
                        except ValueError:
                            print("\033[31mDigita o Hexadecimal certo lek")
                            sleep(1.5)
                            chama_hex_oct()
                        break
                    elif c == 12:
                        try:
                            bina = chama_oct_bin()
                            print("O valor do binario é", bina)
                        except ValueError:
                            print("\033[31mDigita o Octal certo lek")
                            sleep(1.5)
                            chama_oct_bin()
                        break
                    elif c == 11:
                        try:
                            deci = chama_oct_dec()
                            print("O valor do decimal é", deci)
                        except ValueError:
                            print("\033[31mDigita o Octal certo lek")
                            sleep(1.5)
                            chama_oct_dec()
                        break
                    elif c == 10:
                        try:
                            hexa = chama_oct_hex()
                            print("O valor do hexagonal é", hexa)
                        except ValueError:
                            print("\033[31mDigita o Octal certo lek")
                            sleep(1.5)
                            chama_oct_hex()
                        break
                except ValueError:
                    c = 1
        except ValueError:
            print("\033[31mDigite uma entrada valida")
            c = 0


def chama_bin_hex():
    deca = binarios()
    hexa = conversordebase(deca, 16)
    return hexa


def chama_bin_oct():
    deca = binarios()
    octa = conversordebase(deca, 8)
    return octa


def chama_dec_hex():
    deca = eval(input("Digite um numero natural Ex: 4\n"))
    hexa = conversordebase(deca, 16)
    return hexa


def chama_dec_oct():
    deca = eval(input("Digite um numero natural Ex: 4\n"))
    octa = conversordebase(deca, 8)
    return octa


def chama_oct_hex():
    deci = chama_oct_dec()
    hexa = conversordebase(deci, 16)
    print("O valor do hexadecimal é", hexa)
    return hexa


def chama_oct_dec():
    octa = input("Digite um octadecimal\n")
    octa_lista = list(octa)
    deci = 0
    k = 0
    for i in reversed(range(len(octa_lista))):
        try:
            if 0 <= int(octa_lista[i]) <= 7:
                deci += int(octa_lista.pop()) * 8 ** k
                k += 1
        except ValueError:
            print("Digite um octadecimal valido")
            chama_oct_dec()
    return deci


def chama_oct_bin():
    deci = chama_oct_dec()
    bina = conversordebase(deci, 2)
    return bina


def chama_hex_oct():
    deci = chama_hex_dec()
    octa = conversordebase(deci, 8)
    return octa


def chama_hex_dec():
    hexa = input("Digite um hexadecimal\n")
    hexa_lista = list(hexa)
    deci = 0
    hexas = "0123456789ABCDEFabcdef"
    A, B, C, D, E, F = 10, 11, 12, 13, 14, 15
    a, b, c, d, e, f = 10, 11, 12, 13, 14, 15
    for i in range(len(hexa_lista)):
        try:
            if not hexa_lista[i] in hexas:
                print("Digite um hexadecimal valido")
                chama_hex_dec()
        except ValueError:
            print("Digite um hexadecimal valido")
            chama_hex_dec()
    x = 0
    while len(hexa_lista) > 0:
        try:
            if hexa_lista[len(hexa_lista) - 1] in "123456789":
                deci += eval(hexa_lista.pop()) * 16 ** x
                x += 1
            else:
                deci += (eval(hexa_lista.pop()) * (16 ** x))
                x += 1
        except ValueError:
            print("bugo na ultimo try")
    return deci


def chama_hex_bin():
    deci = chama_hex_dec()
    bina = conversordebase(deci, 2)
    return bina


def chama_dec_bin():
    bin_result = dec_bin()
    try:
        if bin_result / int(bin_result) == 1:
            bin_result = int(bin_result)
            return bin_result
    except ValueError:
        bin_result = float(bin_result)
        return bin_result


def dec_bin():
    dec = input("\033[34mDigite um numero inteiro")
    try:
        try:
            if isinstance(int(dec), int):
                dec = int(dec)
                bin_result = dec_bin_nat(dec)
                return int(bin_result)
        except ValueError:
            try:
                bina = list(str(dec))
                try:
                    i = bina.index(".")
                    bina.remove(".")
                    bin_result = bin_instrucao(i, bina)
                    return bin_result
                except ValueError:
                    i = bina.index(",")
                    bina.remove(",")
                    bin_result = bin_instrucao(i, bina)
                    return bin_result
            except ValueError:
                print("\033[31mDigita um decimal anta"
                      "\n")
                sleep(1.5)
                chama_dec_bin()
    except ValueError:
        print("\033[31mDigita um decimal anta"
              "\n")
        sleep(1.5)
        chama_dec_bin()


def bin_instrucao(i, bina):
    dec_list_0 = []
    dec_list_1 = []
    dec_1 = ""
    dec_2 = "0."
    for k in range(0, i):
        dec_list_0.append(bina[k])
    for j in range(i, len(bina)):
        dec_list_1.append(bina[j])
    for k in range(len(dec_list_0)):
        dec_1 += str(dec_list_0[k])
    for k in range(len(dec_list_1)):
        dec_2 += str(dec_list_1[k])
    bin_1 = dec_bin_nat(int(dec_1))
    bin_2 = dec_bin_frac(dec_2)
    bin_result = bin_1 + bin_2
    return bin_result


def dec_bin_nat(dec):
    bina = []
    while dec > 1:
        x = dec % 2
        bina.append(x)
        dec = dec // 2
    bina.append(1)
    bina.reverse()
    binstr: str = str(bina[0])
    for i in range(1, len(bina)):
        binstr += str(bina[i])
    return binstr


def dec_bin_frac(fracao):
    dec_2 = float(fracao)
    bina = "."
    while dec_2 > 0:
        bina += str((int(dec_2 * 2)))
        dec_2 = dec_2 * 2 - int(dec_2 * 2)
    return bina


def binarios():
    string = list(input("\033[34mDigite um numero binario\n"))
    try:
        try:
            try:
                if (string[string.index(",")]) == ",":
                    bin_fracionario(string)
                    sleep(2.5)
            except ValueError:
                if (string[string.index(".")]) == ".":
                    bin_fracionario(string)
                    sleep(2.5)
        except ValueError:
            lista_int = conv_liststr_listint(string)
            for i in range(len(lista_int)):
                if lista_int[i] != 0 and lista_int[i] != 1:
                    print("\033[31mDigite um binario valido")
                    sleep(1.5)
                    binarios()
            dec = convertbindec(lista_int)
            sleep(2.5)
            return dec
    except ValueError:
        print("\033[31;1mTu não sabe binario????")
        sleep(1.5)
        binarios()


def conv_liststr_listint(lista_str):
    lista_int = []
    for k in range(len(lista_str)):
        lista_int.append(int(lista_str[k]))
    for j in range(len(lista_int)):
        if lista_int[j] != 1 and lista_int[j] != 0:
            print("\033[31;1mTu não sabe binario????")
            sleep(1.5)
            binarios()
        else:
            return lista_int


def convertbindec(lista_int: list):
    dec = 0
    for k, r in zip(reversed(range(len(lista_int))), range(len(lista_int))):
        x = lista_int[k] * 2 ** r
        dec = dec + x
    return dec


def bin_fracionario(string: list):
    lista_str1 = []
    lista_str2 = []
    try:
        z = string.index(",")
        string.remove(",")
        for i in range(0, z):
            lista_str1.append(string[i])
        for j in range(z, len(string)):
            lista_str2.append(string[j])
        bin_fracionario_cont(lista_str1, lista_str2)
    except ValueError:
        z = string.index(".")
        string.remove(".")
        for i in range(0, z):
            lista_str1.append(string[i])
        for j in range(z, len(string)):
            lista_str2.append(string[j])
        bin_fracionario_cont(lista_str1, lista_str2)


def bin_fracionario_cont(lista_str1, lista_str2):
    lista_int1 = conv_liststr_listint(lista_str1)
    lista_int2 = conv_liststr_listint(lista_str2)
    for i in range(len(lista_int1)):
        if lista_int1[i] != 1 and lista_int1[i] != 0:
            print("\033[31;1mPô não sabe nem digitar binario\n")
            sleep(1.5)
            entrada()
    for k in range(len(lista_int2)):
        if lista_int2[k] != 1 and lista_int2[k] != 0:
            print("\033[31;1mPô não sabe nem digitar binario\n")
            sleep(1.5)
            entrada()
    dec1 = convertbindec(lista_int1)
    dec2 = bin_frac_dec_frac(lista_int2)
    print("O valor do binario em decimais vale:", dec1 + dec2)


def bin_frac_dec_frac(lista_str2: list):
    dec_frac = 0
    lista_int = conv_liststr_listint(lista_str2)
    for i in range(len(lista_int)):
        dec_frac = lista_int[i] * 2 ** -(i + 1) + dec_frac
    return dec_frac


def conversordebase(dec, base):
    possiveis_in = "0123456789ABCDEF"

    lista = []

    while dec > 0:
        rem = dec % base
        lista.append(rem)
        dec = dec // base

    string_nova = ""
    while len(lista) > 0:
        string_nova = string_nova + possiveis_in[lista.pop()]

    return string_nova


entrada()
