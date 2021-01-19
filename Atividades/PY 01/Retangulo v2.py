def ret():
    larg = int(input("Digite a Largura:"))
    alt = int(input("Digite a Altura:"))
    print("#" * larg)
    alt -= 2
    while alt > 0:
        print("#",' '*(larg-4),'#')
        alt = alt-1
    print("#" * larg)
ret()