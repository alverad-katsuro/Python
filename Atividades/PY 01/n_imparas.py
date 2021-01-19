lista=[]
def main():
 n = int(input("Digite o número de ímpares que você deseja saber!!!: "))
 x = 0
 z = 0
 while x < (n):
  z = z + 1
  if z % 2 != 0:
   x = x + 1
   print(z)
   global lista
   lista.append(z)
