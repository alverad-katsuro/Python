from random import choice, randrange, sample
from math import log

memoria = {0: 1, 1: 12, 2: 4, 3: 14, 4: 4, 5: 12, 6: 8, 7: 6, 8: 10, 9: 14, 10: 0, 11: 0, 12: 2, 13: 179, 14: 1, 15: 163}
memoria_cache = {0: {}, 1: {}}
lista_keys = list(memoria.keys())


class Process:
    def __init__(self):
        self.processador = True
        self.ci = 0
        self.r0 = 0

    def cpu(self):
        while self.ci != -1:
            rem = self.ci
            rdm = Ram.leitura(rem, self.processador)
            ri = rdm
            if ri[0] == 0:  # Break
                self.ci = -1
                break
            elif ri[0] == 1:  # Load
                rdm = Ram.leitura(ri[1], self.processador)
                self.r0 = int(f'{rdm[0]:08b}' + f'{rdm[1]:08b}', 2)
            elif ri[0] == 2:  # STORE?
                pass
            elif ri[0] == 3:  # Soma
                rdm = Ram.leitura(ri[1], self.processador)
                self.r0 = self.r0 + int(f'{rdm[0]:08b}' + f'{rdm[1]:08b}', 2)
            elif ri[0] == 4:  # Subtracao
                rdm = Ram.leitura(ri[1], self.processador)
                self.r0 = self.r0 - int((f'{rdm[0]:08b}' + f'{rdm[1]:08b}'), 2)
            elif ri[0] == 5:  # JZ
                if self.r0 == 0:
                    self.ci = ri[1]
            elif ri[0] == 6:  # JP
                if self.r0 > 0:
                    self.ci = ri[1]
            elif ri[0] == 7:  # JN
                if self.r0 < 0:
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


class Ram:
    def __init__(self, linhas=16, tamanho_celula=8, memo_ram=None):
        if memo_ram is None:
            self.memo_ram = {}
            self.memo_ram = {k: x for k, x in zip(range(linhas), sample(range(randrange(2 ** tamanho_celula)), linhas))}
            self.tamanho_celula = tamanho_celula
            self.tamanho_linhas = int(log(linhas, 2))
        else:
            self.memo_ram = memo_ram
            self.tamanho_linhas = int(log(len(memo_ram), 2))
            maior = memo_ram[list(memo_ram.keys())[0]]
            for k in list(memo_ram.keys()):
                if memo_ram[k] > maior:
                    self.tamanho_celula = round(log(memo_ram[k], 2) + 0.5)

    def leitura(self, endereco=0, processador=False):
        if not processador:
            endere = input("Digite o endereço de 4 bits: ")
            if len(endere) == 4:
                print("\033[35mEndereço: {} Dado: {}".format(f'{endere:0b}'.zfill(self.tamanho_linhas),
                                                             f'{self.memo_ram[endere]:0b}'.zfill(self.tamanho_celula)))
            else:
                print("\033[31mDigite um endereço valido")
                Ram.leitura()
        else:
            pass

    def escrita_ram(self, endereco=0, processador=False):
        if not processador:
            while len(str(endereco)) < self.tamanho_linhas:
                endereco = eval(input(f"Digite o endereço de {self.tamanho_linhas} bits: "))
                celula = 0
                while len(str(celula)) < self.tamanho_celula:
                    celula = eval(input(f"Digite o dado de {self.tamanho_celula} bits: "))
                    assert isinstance(celula, int), isinstance(endereco, int)
                    self.memo_ram.update({endereco: celula})
        else:
            pass


class Cache:
    def __init__(self, ram_obj, conjuntos=2, linhas=8, dados=2, memo=None):
        if linhas % 2 != 0:
            linhas += 1
        assert linhas % 2 == 0
        if dados % 2 != 0:
            dados += 1
        assert log(conjuntos, 2) == float(int(log(conjuntos, 2))), log(dados, 2) == float(int(log(dados, 2)))
        self.ram_obj = ram_obj
        if memo is None:
            self.conjuntos = conjuntos
            self.linhas = linhas
            self.dados = dados
            self.tag = int(linhas / conjuntos)
            self.memo_cache = {}
        else:
            self.tag = len(memo[0])
            self.conjuntos = len(memo)
            self.dados = len(memo[0][list(memo[0].keys())[0]])
        Cache.memo_cache_random(self)

    def memo_cache_random(self):
        for c in range(self.conjuntos):
            self.memo_cache.update({c: {}})
            while len(self.memo_cache[c]) != self.tag:
                escolha = choice(list(self.ram_obj.memo_ram.keys()))
                tag = escolha >> (int(log(self.dados + self.conjuntos, 2)))
                if tag not in self.memo_cache[c] and escolha in range(self.dados * c,
                                                                      2 ** self.ram_obj.tamanho_linhas,
                                                                      self.dados * self.conjuntos):
                    self.memo_cache[c].update({tag: {}})
                    while len(self.memo_cache[c][tag]) != self.dados:
                        for d in reversed(range(self.dados)):
                            self.memo_cache[c][tag].update({d: self.ram_obj.memo_ram[escolha]})

    def memo_cache_escrita(self, processador=False):
        if not processador:
            endereco = 0
            while len(str(endereco)) < self.ram_obj.tamanho_linhas:
                endereco = input(f"Digite o endereço de {self.ram_obj.tamanho_linhas} bits: ")
                celula = 0
                while len(str(celula)) < self.ram_obj.tamanho_celula:
                    celula = int((input(f"Digite o dado de {self.ram_obj.tamanho_celula} bits: ")), 2)
                    assert isinstance(celula, int)
                    conj, tag, dado = Cache.mani_dados(endereco)
                    self.memo_cache[conj][tag][dado].update({endereco: celula})
        else:
            pass

    def mani_dados(self, endereco):
        conj = int(endereco[-self.conjuntos:], 2)
        tag = int(endereco[:self.tag], 2)
        dado = int(endereco[tag:-conj], 2)
        return conj, tag, dado


def ler_tudo(memo_cache_object):
    cel = memo_cache_object.ram_obj.tamanho_celula
    lin = memo_cache_object.ram_obj.tamanho_linhas
    print("Na Memória cahce está armazenado")
    for c in range(memo_cache_object.conjuntos):
        for tag in range(memo_cache_object.tag):
            dado = ""
            for d in reversed(range(memo_cache_object.dados)):
                dado += f' Dado {d}: ' + f'{memo_cache_object.memo_cache[c][tag][d]:0b}'.zfill(cel)
            print("Tag: {0} Conjunto: {1} {2}".format(f'{tag}'.zfill(cel), f'{c}'.zfill(cel), dado))
    print("Na MP temos")
    for enderecos in range(len(memo_cache_object.ram_obj.memo_ram.keys())):
        print("Endereço: {} Dado: {}".format(f'{enderecos:0b}'.zfill(lin),
                                             f'{memo_cache_object.ram_obj.memo_ram[enderecos]:0b}'.zfill(cel)))


def ler(memo_cache_object):
    endereco = 0
    while len(str(endereco)) < memo_cache_object.ram_obj.tamanho_linhas:
        endereco = input(f"Digite o endereço de {memo_cache_object.ram_obj.tamanho_linhas} bits: ")
        conj, tag, dado = Cache.mani_dados(endereco)
        if conj in memo_cache_object.memo_cache:
            if tag in memo_cache_object[conj]:
                if dado in memo_cache_object[conj][tag]:
                    print("O dado está na MC")
                    print("Endereço: {} Tag: {} Conjunto: {} Dado {}".format(endereco,
                                                                             tag,
                                                                             conj,
                                                                             memo_cache_object.
                                                                             ram_obj.memo_cache[conj][tag][dado]))
                    return None
        else:
            print("O dado está na MP")
            print("Endereço: {} Dado: {}".format(f'{endereco:0b}'.zfill(memo_cache_object.ram_obj.
                                                                        tamanho_linhas.memo_cache_object.
                                                                        ram_obj.memo_ram[int(endereco, 2)]),
                                                 f'{memo_cache_object.ram_obj.tamanho_celula:0b}'.
                                                 zfill(memo_cache_object.ram_obj.tamanho_celula)))


ram = Ram()
cache = Cache(ram)
controle = "w"
while controle in "WwRrLlPp":
    processador = False
    controle = input("\033[34mDigite:\nW - Write\nR - READER"
                     "\nL - READ ALL\nP para executar instruções\nQualquer tecla para parar\n")
    if (controle == "W") or (controle == "w"):
        ram.escrita_ram()
    elif (controle == "R") or (controle == "r"):
        ram.leitura()
    elif (controle == "L") or (controle == "l"):
        ler_tudo(cache)
    elif (controle == "P") or (controle == "p"):
        a = Process()
        a.cpu()
    else:
        pass
