import re


def le_assinatura():
    # A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos
    # fornecidos
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    # A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    return textos


def separa_sentencas(texto):
    # A funcao recebe um texto e devolve uma lista das sentencas dentro do texto
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    # A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    # A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    # Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    # Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def menor_assinatura(Sab):
    menor = Sab[0]
    for k in range(len(Sab)):
        if menor > Sab[k]:
            menor = Sab
    return menor


def compara_assinatura(as_a, as_b):
    Sab = []
    for k in range(len(as_a)):
        Sab.append(abs(as_a[k] - as_b[k]))
    return sum(Sab) / 6

def calc_wal(palavras):
    n_palavras = len(palavras)
    n_letras = 0
    for k in range(n_palavras):
        n_letras += len(palavras[k])
    return n_letras / n_palavras


def calc_ttr(palavras):
    pala_dif = n_palavras_diferentes(palavras)
    return pala_dif / len(palavras)


def calc_hlr(palavras):
    pala_unic = n_palavras_unicas(palavras)
    return pala_unic / len(palavras)


def calc_sal(sentencas):
    n_letras = 0
    for k in range(len(sentencas)):
        x = len(sentencas[k])
        n_letras += x
    return n_letras / len(sentencas)


def calc_sac(sentencas, frase):
    return len(frase) / len(sentencas)


def calc_pal(frase):
    n_letras = 0
    for k in range(len(frase)):
        x = len(frase[k])
        n_letras += x
    return n_letras / len(frase)


def calcula_assinatura(texto):
    # IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    calc_final = []
    sentencas = separa_sentencas(texto)
    frase = sep_text(sentencas)
    palavras = sep_frases(frase)
    calc_final.append(calc_wal(palavras))
    calc_final.append(calc_ttr(palavras))
    calc_final.append(calc_hlr(palavras))
    calc_final.append(calc_sal(sentencas))
    calc_final.append(calc_sac(sentencas, frase))
    calc_final.append(calc_pal(frase))
    return calc_final


def sep_frases(frase):
    if type(frase) is list:
        palavras = []
        for k in range(len(frase)):
            new = separa_palavras(frase[k])
            palavras += new
        return palavras
    else:
        return separa_palavras(frase)


def sep_text(text):
    if type(text) is list:
        frases = []
        for k in range(len(text)):
            new = separa_frases(text[k])
            frases += new
        return frases
    else:
        return separa_frases(text)


def avalia_textos(texto, ass_cp):
    # IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do
    # texto com maior probabilidade de ter sido infectado por COH-PIAH.
    if len(texto) > 1:
        tex = 0
        avalia_list = []
        for k in range(len(texto)):
            ass_1 = calcula_assinatura(texto[k])
            avalia_list.append(ass_1)
        menor = compara_assinatura((avalia_list[0]), ass_cp)
        for i in range(len(avalia_list)):
            z = compara_assinatura((avalia_list[i]), ass_cp)
            if menor >= z:
                menor = z
                tex = i + 1
        return tex
    else:
        return compara_assinatura(ass_1,ass_cp)
