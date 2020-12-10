def main():
 import sys
 x = int(input("Vamos calcular fatorias\nDigite um numero fatorial: "))
 if x >= 2:
  y = x - 1
  fatorial = (x * y)
  while y > 1:
   y = y - 1
   fatorial = fatorial * y
  print(fatorial)
 else:
  if x >= 0:
   print(1)
  else:
   print("Não existe fatorial negativo!!!")
main()
