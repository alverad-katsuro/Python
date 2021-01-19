nova =[]
def remove_repetidos(lista):
    global nova
    lista.sort()
    for x in lista:
        if nova.count(x)==0:
            nova.append(x)
    lista=nova
    return nova
