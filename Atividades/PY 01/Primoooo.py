def n_primos(x):
    continuar = 1
    count = 0
    while continuar ==1:
        for aqui in reversed(range(2,x+1)):
            if all(aqui%d !=0 for d in range(2,aqui)):
                count += 1
        return count
        continuar = 0
