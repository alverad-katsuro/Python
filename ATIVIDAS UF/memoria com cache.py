from random import choice, sample, randint
from math import log


class Process:
    def __init__(self, memo_cache_object):
        self.processador = False
        self.ci = 0
        self.r0 = 0
        self.ri = 0
        self.rem = None
        self.rdm = 0
        self.rdm_s = 0
        self.cache = memo_cache_object

    def instrucoes(self):
        self.processador = True
        while self.ci != -1:
            self.rem = self.ci
            self.ler()
            self.rem = int(f'{self.rdm:016b}'[8:16], 2)
            self.ri = int(f'{self.rdm:016b}'[0:8], 2)
            self.rdm_s = ["Dado 0:", self.ri, "Dado 1:", int(f'{self.rdm:016b}'[8:16], 2)]
            if self.ri == 0:  # Break
                self.ci = -1
                self.processador = False
            elif self.ri == 1:  # Load
                self.ler()
                self.r0 = self.rdm
                self.ci += 2
            elif self.ri == 2:  # STORE?
                self.ci += 2
                # k = [int(f'{self.r0:016b}'[0:8], 2), int(f'{self.r0:016b}'[8:16], 2)] #sla pra q
            elif self.ri == 3:  # Soma
                self.ler()
                self.r0 = self.r0 + self.rdm
                self.ci += 2
            elif self.ri == 4:  # Subtracao
                self.ler()
                self.r0 = self.r0 - self.rdm
                self.ci += 2
            elif self.ri == 5:  # JZ
                if self.r0 == 0:
                    self.ci = int(f'{self.rdm:016b}'[8:16], 2)
                else:
                    self.ci += 2
            elif self.ri == 6:  # JP
                if self.r0 > 0:
                    self.ci = int(f'{self.rdm:016b}'[8:16], 2)
                else:
                    self.ci += 2
            elif self.ri == 7:  # JN
                if self.r0 < 0:
                    self.ci = int(f'{self.rdm:016b}'[8:16], 2)
                else:
                    self.ci += 2
            elif self.ri == 8:  # JUMP
                self.ci = int(f'{self.rdm:016b}'[8:16], 2)
            elif self.ri == 9:  # GET
                self.ci += 2
                self.rdm = int(input("Digite um binario de 16 bits"), 2)
            elif self.ri == 10:  # PRINT
                self.memo_cache_escrita()
                self.ci += 2
            else:
                print("Algo deu erro")
                self.ci = -1
            self.ri = 0

    def validacao(self):
        endereco = input(f"Digite o endereço de {self.cache.ram.tamanho_linhas} bits: ")
        while len(str(endereco)) != self.cache.ram.tamanho_linhas:
            endereco = input(f"Digite o endereço de {self.cache.ram.tamanho_linhas} bits: ")
        celula = input(f"Digite o dado de {self.cache.ram.tamanho_celula} bits: ")
        while len(str(celula)) != self.cache.ram.tamanho_celula:
            celula = int((input(f"Digite o dado de {self.cache.ram.tamanho_celula} bits: ")), 2)
        celula = int(celula, 2)
        return endereco, celula

    def mani_dados(self, endereco):
        if type(endereco) == int:
            endereco = f'{endereco:0b}'.zfill(self.cache.ram.tamanho_linhas)
        conj = int(endereco[-(self.cache.bit_conjuntos + self.cache.bit_dados):-self.cache.bit_dados], 2)
        tag = int(endereco[:self.cache.tag_bit], 2)
        dado = int(endereco[-self.cache.bit_dados:], 2)
        return conj, tag, dado

    def ler_tudo(self):
        cel = self.cache.ram.tamanho_celula
        lin = self.cache.ram.tamanho_linhas
        print("\033[33mNa Memória cache está armazenado")
        for c in range(self.cache.conjuntos):
            for tag in list(self.cache.memo_cache[c].keys()):
                dado = ""
                for d in reversed(range(self.cache.dados)):
                    dado += f' Dado {d}: ' + f'{self.cache.memo_cache[c][tag][d]:0b}'.zfill(self.cache.
                                                                                            ram.tamanho_celula)
                print("Tag: {} Conjunto: {}{}".format(f'{tag:0b}'.zfill(self.cache.tag_bit), f'{c:0b}'.
                                                      zfill(int(log(self.cache.conjuntos, 2))), dado))
        print("\033[35m\nNa MP temos")
        for enderecos in range(len(self.cache.ram.memo_ram.keys())):
            print("Endereço: {} Dado: {}".format(f'{enderecos:0b}'.zfill(lin),
                                                 f'{self.cache.ram.memo_ram[enderecos]:0b}'.zfill(cel)))

    def ler(self):
        if not self.processador:
            endereco = input(f"Digite o endereço de {self.cache.ram.tamanho_linhas} bits: ")
            while len(str(endereco)) != self.cache.ram.tamanho_linhas:
                endereco = input(f"Digite o endereço de {self.cache.ram.tamanho_linhas} bits: ")
            conj, tag, dado = self.mani_dados(endereco)
            if conj in self.cache.memo_cache and tag in self.cache.memo_cache[conj] \
                    and dado in self.cache.memo_cache[conj][tag]:
                print("\033[33mO dado está na MC")
                print("Tag: {} Conjunto: {} Dado {}: {}".format(f'{tag:0b}'.zfill(self.cache.tag_bit),
                                                                f'{conj:0b}'.zfill(self.cache.bit_conjuntos),
                                                                f'{dado:0b}'.zfill(len(endereco[self.cache.tag_bit:-self
                                                                                       .cache.bit_conjuntos])),
                                                                f'{self.cache.memo_cache[conj][tag][dado]:0b}'.
                                                                zfill(self.cache.ram.tamanho_celula)))
            else:
                print("\033[35mO dado está na MP")
                print("Endereço: {} Dado: {}".format(endereco, f'{self.cache.ram.memo_ram[int(endereco, 2)]:0b}'
                                                     .zfill(self.cache.ram.tamanho_celula)))
        else:
            endereco = f'{self.rem:0b}'.zfill(self.cache.ram.tamanho_linhas)
            conj, tag, dado = self.mani_dados(endereco)
            if conj in self.cache.memo_cache and tag in self.cache.memo_cache[conj] \
                    and dado in self.cache.memo_cache[conj][tag]:
                rdm = int((f'{self.cache.memo_cache[conj][tag][0]:08b}'
                          + f'{self.cache.memo_cache[conj][tag][1]:08b}'), 2)
                self.rdm = rdm
            else:
                self.memo_cache_escrita()

    def inscricao(self, endereco, conj, tag, dado, celula=0):
        if type(endereco) == int:
            endereco = f'{endereco:0b}'.zfill(self.cache.ram.tamanho_linhas)
            endereco_att_ram = int(endereco, 2)
            self.escrita_cache(endereco, endereco_att_ram, conj, tag, dado, celula)
        else:
            endereco_att_ram = endereco
            self.escrita_cache(endereco, endereco_att_ram, conj, tag, dado, celula)

    def escrita_cache(self, endereco, endereco_att_ram, conj, tag, dado, celula):
        if tag not in self.cache.memo_cache[conj] and not self.processador:
            self.load_ram_cache(endereco, conj, tag)
            self.cache.memo_cache[conj][tag][dado] = celula
            self.cache.ram.memo_ram[endereco_att_ram] = celula
        elif tag in self.cache.memo_cache[conj] and self.processador and self.ri == 10:
            self.cache.memo_cache[conj][tag][dado] = celula
            self.cache.ram.memo_ram[endereco_att_ram] = celula
        elif tag not in self.cache.memo_cache[conj] and self.processador and self.ri == 10:
            self.load_ram_cache(endereco, conj, tag)
            self.cache.memo_cache[conj][tag][dado] = celula
            self.cache.ram.memo_ram[endereco_att_ram] = celula
        else:
            self.load_ram_cache(endereco, conj, tag)

    def load_ram_cache(self, endereco, conj, tag):
        escolha = choice(list(self.cache.memo_cache[conj].keys()))
        del (self.cache.memo_cache[conj][escolha])
        self.cache.memo_cache[conj].update({tag: {}})
        endereco = int(endereco, 2) >> self.cache.bit_dados
        endereco = endereco << self.cache.bit_dados
        endereco = endereco + (self.cache.dados - 1)
        for k in reversed(range(self.cache.dados)):
            self.cache.memo_cache[conj][tag].update({k: self.cache.ram.memo_ram[endereco]})
            endereco -= 1

    def memo_cache_escrita(self):
        if not self.processador:
            endereco, celula = self.validacao()
            assert isinstance(celula, int)
            conj, tag, dado = self.mani_dados(endereco)
            self.inscricao(endereco, conj, tag, dado, celula)
        else:
            if self.ri == 10:
                p = 0
                celula = [int(f'{self.r0:016b}'[0:8], 2), int(f'{self.r0:016b}'[8:16], 2)]
                for c in celula:
                    conj, tag, dado = self.mani_dados(self.rem + p)
                    self.inscricao(self.rem + p, conj, tag, dado, c)
                    p += 1
                print("Dado:", f'{celula[0]:08b}' + f'{celula[1]:08b}')
            else:
                conj, tag, dado = self.mani_dados(f'{self.rem:0b}'
                                                  .zfill(self.cache.ram.tamanho_linhas))
                self.inscricao(self.rem, conj, tag, dado)
                n = []
                for d in range(self.cache.dados):
                    n.append(self.cache.memo_cache[conj][tag][d])
                self.rdm = int(f'{n[0]:08b}' + f'{n[1]:08b}', 2)


class Ram:
    def __init__(self, bit_linhas=5, tamanho_celula=8, memo_ram=None):
        if memo_ram is None:
            self.tamanho_linhas = bit_linhas
            self.linhas = 2 ** self.tamanho_linhas
            self.tamanho_celula = tamanho_celula
            self.memo_ram = {k: x for k, x in zip(range(self.linhas), [z for z in
                                                                       sample(range(randint(self.linhas,
                                                                                            2 ** self.tamanho_celula)),
                                                                              self.linhas)])}
        else:
            self.memo_ram = memo_ram
            self.tamanho_linhas = round(log(len(memo_ram), 2) + 0.4)
            maior = memo_ram[list(memo_ram.keys())[0]]
            for k in list(memo_ram.keys()):
                if memo_ram[k] > maior:
                    self.tamanho_celula = round(log(memo_ram[k], 2) + 0.4)

    def leitura(self):
        endere = input("Digite o endereço de 4 bits: ")
        if len(endere) == 4:
            print("\033[35mEndereço: {} Dado: {}".format(f'{endere:0b}'.zfill(self.tamanho_linhas),
                                                         f'{self.memo_ram[endere]:0b}'.zfill(self.tamanho_celula)))
        else:
            print("\033[31mDigite um endereço valido")
            self.leitura()

    def escrita_ram(self, endereco=0):
        while len(str(endereco)) < self.tamanho_linhas:
            endereco = eval(input(f"Digite o endereço de {self.tamanho_linhas} bits: "))
            celula = 0
            while len(str(celula)) < self.tamanho_celula:
                celula = eval(input(f"Digite o dado de {self.tamanho_celula} bits: "))
                assert isinstance(celula, int), isinstance(endereco, int)


class Cache:
    def __init__(self, ram_obj, bit_conjuntos=1, bit_linhas=2, bit_dados=1, memo=None):
        self.ram = ram_obj
        if memo is None:
            self.memo_cache = {}
            self.bit_conjuntos = bit_conjuntos
            self.bit_dados = bit_dados
            self.bit_linhas = bit_linhas
            self.conjuntos = 2 ** self.bit_conjuntos
            self.linhas = 2 ** self.bit_linhas
            self.dados = 2 ** self.bit_dados
            self.tag_bit = self.ram.tamanho_linhas - (bit_dados + bit_conjuntos)
            self.tag = 2 ** self.tag_bit
            self.memo_cache_random()
        else:
            self.conjuntos = len(memo)
            self.dados = len(memo[0][list(memo[0].keys())[0]])
            self.bit_conjuntos = int(log(self.conjuntos, 2))
            self.bit_dados = int(log(self.dados, 2))
            self.tag_bit = self.ram.tamanho_linhas - (self.bit_dados + self.bit_conjuntos)
            self.tag = 2 ** self.tag_bit

    def memo_cache_random(self):
        for c in range(self.conjuntos):
            self.memo_cache.update({c: {}})
            while len(self.memo_cache[c]) < self.linhas / self.conjuntos:
                escolha = choice(list(self.ram.memo_ram.keys()))
                tag = escolha >> (int(log(self.dados + self.conjuntos, 2)))
                if tag not in self.memo_cache[c] and escolha in range(self.dados * c,
                                                                      2 ** self.ram.tamanho_linhas,
                                                                      self.dados * self.conjuntos):
                    self.memo_cache[c].update({tag: {}})
                    while len(self.memo_cache[c][tag]) != self.dados:
                        for d in reversed(range(self.dados)):
                            self.memo_cache[c][tag].update({d: self.ram.memo_ram[escolha+d]})


def situacao(u):
    if u == 1:
        memoria = {0: 1, 1: 14, 2: 4, 3: 16, 4: 7, 5: 10, 6: 10, 7: 14, 8: 8, 9: 12,
                   10: 10, 11: 14, 12: 0, 13: 0, 14: 2, 15: 179, 16: 1, 17: 163}
        ram = Ram(0, 0, memoria)
        cache = Cache(ram)
        cpu = Process(cache)
        control(cpu)
    elif u == 2:
        memoria = {0: 10, 1: 18, 2: 1, 3: 18, 4: 4, 5: 16, 6: 2, 7: 18, 8: 10, 9: 18,
                   10: 5, 11: 14, 12: 8, 13: 4, 14: 0, 15: 0, 16: 0, 17: 1, 18: 0, 19: 10}
        ram = Ram(0, 0, memoria)
        cache = Cache(ram)
        cpu = Process(cache)
        cpu.ci = 2
        control(cpu)
    else:
        ram = Ram()
        cache = Cache(ram)
        cpu = Process(cache)
        control(cpu)


def control(cpu):
    memoria = {0: 10, 1: 18, 2: 1, 3: 18, 4: 4, 5: 16, 6: 2, 7: 18, 8: 10, 9: 18,
               10: 5, 11: 14, 12: 8, 13: 4, 14: 0, 15: 0, 16: 0, 17: 1, 18: 0, 19: 10}
    v = 0
    while v == 0:
        controle = input("\n\033[34mDigite:\nW - Write\nR - READER"
                         "\nL - READ ALL\nP para executar instruções\n"
                         "V para voltar\nQualquer tecla para acessar o console\n")
        if (controle == "W") or (controle == "w"):
            cpu.memo_cache_escrita()
        elif (controle == "R") or (controle == "r"):
            cpu.ler()
        elif (controle == "L") or (controle == "l"):
            cpu.ler_tudo()
        elif (controle == "P") or (controle == "p"):
            if cpu.cache.ram.memo_ram == memoria:
                print(f'Dado: {10:016b}')
            cpu.instrucoes()
        elif (controle == "V") or (controle == "v"):
            v = 1
        else:
            pass

def start():
    menu = "w"
    while menu in "WwRrLlPpVv":
        b = input("\n\033[34mDigite\n1. Exemplo 1\n2. Exemplo 2\n3. Aleatorio\n")
        situacao(int(b))


start()
