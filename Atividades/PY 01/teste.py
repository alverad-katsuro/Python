def main( ):
    n = input ("Digite o nome do cliente: ")
    d = input ("Digite o dia de vencimento: ")
    m = input ('Digite o mês de vencimento: ')
    v = input ('Digite o valor da fatura: ')

    print("Olá,", n,
"A sua fatura com vencimento em", d, "de", m, "no valor de R$", v, "está fechada.")
main()

def beta():
    '''
    Programa que lê uma sequência de números inteiros
    não nulos e imprime o quadrado d cada número lido.

    Exemplo de execução:
    >>> 
    Cálculo dos quadrados de uma sequência de números.
    A sequência termina com um 0 (zero).

    Digite um número: 3
    3 ao quadrado é 9
    Digite um número: -5
    -5 ao quadrado é 25
    Digite um número: 12
    12 ao quadrado é 144
    Digite um número: 0
    >>> 
    '''

    print("Cálculo dos quadrados de uma sequência de números.")
    print("A sequência termina com um 0 (zero).\n")
    
    num = int(input("Digite um número: "))
    while num != 0:
        quadrado = num * num
        print(num, "ao quadrado é", quadrado)
        num = int(input("Digite um número: "))

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
beta()
