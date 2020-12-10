continuar = 1
count = 0
while continuar ==1:
    x = continuar =int(input("Digite uma sequencia de algarismos para saber a quanditade de numeros primos nela contido\n"))
    for aqui in reversed(range(1,x+1)):
        if all(aqui%d !=0 for d in range(2,aqui)):
            count += 1
    print(count)