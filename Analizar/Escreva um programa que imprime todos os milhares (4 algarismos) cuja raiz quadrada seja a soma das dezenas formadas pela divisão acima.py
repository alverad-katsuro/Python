n = int(input("Digite o valor de n: "))
adjiguais = False
ant = n%10
n = n//10
while n > 0:
    r = n%10
    if ant == r:
        adjiguais = True
    ant = r
    n = n//10
if adjiguais:
    print("Contém adjacentes iguais")
else:
    print("Não contém adjacentes iguais")