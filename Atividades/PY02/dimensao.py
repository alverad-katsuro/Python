def dimensoes(matriz):
    linha = len(matriz)
    try:
        coluna = len(matriz[0])
        print(f"{linha}x{coluna}")
    except TypeError:
        print(f"{linha}x{linha}")
