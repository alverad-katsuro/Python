from random import choice, sample, randint
from math import log

class Process:
    def __init__(self, memo_cache_object):
        self.processador = False
        self.ci = 0
        self.r0 = 0
        self.cache = memo_cache_object

    def instrucoes(self):
        self.processador = True
        while self.ci != -1:
            print(self.ci)
            self.rem = self.ci
            rdm = Process.ler(self)
            ri = rdm
            if ri[0] == 0:  # Break
                self.ci = -1
                self.processador = False
                break
            elif ri[0] == 1:  # Load
                self.rem = ri[1]
                rdm = Process.ler(self)
                self.r0 = int(f'{rdm[0]:08b}' + f'{rdm[1]:08b}', 2)
                print(self.r0)
                self.ci += 2
            elif ri[0] == 2:  # STORE?
                pass
            elif ri[0] == 3:  # Soma
                self.rem = ri[1]
                rdm = Process.ler(self)
                self.r0 = self.r0 + int(f'{rdm[0]:08b}' + f'{rdm[1]:08b}', 2)
                self.ci += 2
            elif ri[0] == 4:  # Subtracao
                self.rem = ri[1]
                rdm = Process.ler(self)
                self.r0 = self.r0 - int((f'{rdm[0]:08b}' + f'{rdm[1]:08b}'), 2)
                self.ci += 2
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
                self.ci += 2
                pass
            elif ri[0] == 10:  # PRINT
                self.ci += 2
                pass
            else:
                print("Algo deu erro")
                break


    def validacao(self):
        endereco = input(f"Digite o endereço de {self.cache.ram.tamanho_linhas} bits: ")
        while len(str(endereco)) < self.cache.ram.tamanho_linhas:
            endereco = input(f"Digite o endereço de {self.cache.ram.tamanho_linhas} bits: ")
        celula = int((input(f"Digite o dado de {self.cache.ram.tamanho_celula} bits: ")), 2)
        while len(str(celula)) < self.cache.ram.tamanho_celula:
            celula = int((input(f"Digite o dado de {self.cache.ram.tamanho_celula} bits: ")), 2)
        return endereco, celula

    def mani_dados(self, endereco):
        conj_t = int(log(self.cache.conjuntos, 2))
        tag_t = self.cache.tag_bit
        conj = int(endereco[-conj_t:], 2)
        tag = int(endereco[:tag_t], 2)
        dado = int(endereco[tag_t:-conj_t], 2)
        return conj_t, tag_t, conj, tag, dado

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
                print("Tag: {0} Conjunto: {1}{2}".format(f'{tag:0b}'.zfill(self.cache.tag_bit), f'{c:0b}'.
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
            conj_t, tag_t, conj, tag, dado = Process.mani_dados(self, endereco)
            if conj in self.cache.memo_cache and tag in self.cache.memo_cache[conj] \
                    and dado in self.cache.memo_cache[conj][tag]:
                print("\033[33mO dado está na MC")
                print("Tag: {} Conjunto: {} Dado {}: {}".format(f'{tag:0b}'.zfill(tag_t),
                                                                f'{conj:0b}'.zfill(conj_t),
                                                                f'{dado:0b}'.zfill(len(endereco[tag_t:-conj_t])),
                                                                f'{self.cache.memo_cache[conj][tag][dado]:0b}'.
                                                                zfill(self.cache.ram.tamanho_celula)))
                return None
            else:
                print("\033[35mO dado está na MP")
                print("Endereço: {} Dado: {}".format(endereco, f'{self.cache.ram.memo_ram[int(endereco, 2)]:0b}'
                                                     .zfill(self.cache.ram.tamanho_celula)))
        else:
            endereco = '{}'.format(f'{self.rem:0b}'.zfill(self.cache.ram.tamanho_linhas))
            conj_t, tag_t, conj, tag, dado = Process.mani_dados(self, endereco)
            if conj in self.cache.memo_cache and tag in self.cache.memo_cache[conj] \
                    and dado in self.cache.memo_cache[conj][tag]:
                return self.cache.memo_cache[conj][tag][0], self.cache.memo_cache[conj][tag][1]
            else:
                return Process.memo_cache_escrita(self)

    def inscricao(self, endereco, conj_t, tag_t, conj, tag, dado, celula=0):
        if tag not in self.cache.memo_cache[conj]:
            escolha = choice(list(self.cache.memo_cache[conj].keys()))
            del (self.cache.memo_cache[conj][escolha])
            self.cache.memo_cache[conj].update({tag: {}})
            endereco = int(endereco, 2) >> int(log(self.cache.dados, 2))
            endereco = endereco << int(log(self.cache.dados, 2))
            for k in reversed(range(self.cache.dados)):
                self.cache.memo_cache[conj][tag].update({k: self.cache.ram.memo_ram[endereco]})
                endereco += 1
            if not self.processador:
                self.cache.memo_cache[conj][tag][dado] = celula

    def memo_cache_escrita(self):
        if not self.processador:
            endereco, celula = Process.validacao(self)
            assert isinstance(celula, int)
            conj_t, tag_t, conj, tag, dado = Process.mani_dados(self, endereco)
            Process.inscricao(self, endereco, conj_t, tag_t, conj, tag, dado, celula)

        else:
            conj_t, tag_t, conj, tag, dado = Process.mani_dados(self, f'{self.rem:0b}'
                                                                .zfill(self.cache.ram.tamanho_linhas))
            Process.inscricao(self, f'{self.rem:0b}'.zfill(self.cache.ram.tamanho_linhas),
                              conj_t, tag_t, conj, tag, dado)
            x = []
            for d in reversed(range(self.cache.dados)):
                x.append(self.cache.memo_cache[conj][tag][d])
            return x

class Ram:
    def __init__(self, linhas=32, tamanho_celula=8, memo_ram=None):
        if memo_ram is None:
            self.memo_ram = {k: x for k, x in zip(range(linhas), [x for x in sample(range(randint(linhas,
                                                                                    2 ** tamanho_celula)),
                                                                                    linhas)])}
            self.tamanho_celula = tamanho_celula
            self.tamanho_linhas = int(log(linhas, 2))
        else:
            self.memo_ram = memo_ram
            self.tamanho_linhas = int(log(len(memo_ram), 2))
            maior = memo_ram[list(memo_ram.keys())[0]]
            for k in list(memo_ram.keys()):
                if memo_ram[k] > maior:
                    self.tamanho_celula = round(log(memo_ram[k], 2) + 0.5)

    def leitura(self):
        endere = input("Digite o endereço de 4 bits: ")
        if len(endere) == 4:
            print("\033[35mEndereço: {} Dado: {}".format(f'{endere:0b}'.zfill(self.tamanho_linhas),
                                                         f'{self.memo_ram[endere]:0b}'.zfill(self.tamanho_celula)))
        else:
            print("\033[31mDigite um endereço valido")
            Ram.leitura(self)

    def escrita_ram(self, endereco=0):
        while len(str(endereco)) < self.tamanho_linhas:
            endereco = eval(input(f"Digite o endereço de {self.tamanho_linhas} bits: "))
            celula = 0
            while len(str(celula)) < self.tamanho_celula:
                celula = eval(input(f"Digite o dado de {self.tamanho_celula} bits: "))
                assert isinstance(celula, int), isinstance(endereco, int)


class Cache:
    def __init__(self, ram_obj, conjuntos=2, linhas=4, dados=2, memo=None):
        if linhas % 2 != 0:
            linhas += 1
        assert linhas % 2 == 0
        if dados % 2 != 0:
            dados += 1
        assert log(conjuntos, 2) == float(int(log(conjuntos, 2))), log(dados, 2) == float(int(log(dados, 2)))
        self.ram = ram_obj
        if memo is None:
            self.conjuntos = conjuntos
            self.linhas = linhas
            self.dados = dados
            self.tag_bit = int(log(len(self.ram.memo_ram), 2)) - int(log(conjuntos + dados, 2))
            self.tag = 2 ** self.tag_bit
            self.memo_cache = {}
        else:
            self.tag_bit = int(log(len(self.ram.memo_ram), 2)) - int(log(conjuntos + dados, 2))
            self.tag = 2 ** self.tag_bit
            self.conjuntos = len(memo)
            self.dados = len(memo[0][list(memo[0].keys())[0]])
        Cache.memo_cache_random(self)

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
                            self.memo_cache[c][tag].update({d: self.ram.memo_ram[escolha]})


memoria = {0: 1, 1: 14, 2: 4, 3: 16, 4: 7, 5: 10, 6: 10, 7: 14, 8: 8, 9: 12,
           10: 10, 11: 16, 12: 0, 13: 0, 14: 2, 15: 179, 16: 10, 17: 163}
ram = Ram(0, 0, memoria)
cache = Cache(ram)
cpu = Process(cache)
controle = "w"
while controle in "WwRrLlPp":
    processador = False
    controle = input("\033[34mDigite:\nW - Write\nR - READER"
                     "\nL - READ ALL\nP para executar instruções\nQualquer tecla para parar\n")
    if (controle == "W") or (controle == "w"):
        ram.escrita_ram()
    elif (controle == "R") or (controle == "r"):
        cpu.ler()
    elif (controle == "L") or (controle == "l"):
        cpu.ler_tudo()
    elif (controle == "P") or (controle == "p"):
        cpu.instrucoes()
    else:
        pass
