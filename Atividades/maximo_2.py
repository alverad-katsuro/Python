def variaveis():
 print("Vamos descobrir qual número e maior")
 x = int(input("Digite o primeiro número: "))
 y = int(input("Digite o segundo número: "))
 maximo(x,y)
 
def maximo(x,y):
 if x != y:
  if x > y:
   return x
  else:
   return y
 else:
  return x
variaveis()