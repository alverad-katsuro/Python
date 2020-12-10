z = "sim"
while z == "sim":
 x = input()
 if x == "não":
     break
 else:
     list(listaDeInteiros) + int(x)
todosSaoPares = True
for i in listaDeInteiros:
    if i % 2 == 0:
        todosSaoPares = False
        break
if todosSaoPares:
    print('Todos sao pares')
else:
    print('Tem algum impar')