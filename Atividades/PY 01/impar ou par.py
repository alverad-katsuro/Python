def main ():
 print("Vamos descobrir quantos números são par ou ímpar")
 x = int(input("Digite todos os números e termine com 0\n"))
 ímpar = 0
 par = 0
 while x != 0:
  if x % 2 == 1:
   ímpar = ímpar + (x/x)
   x = int(input("Digite todos os números e termine com 0\n"))
  else:
   par = par + (x/x)
   x = int(input("Digite todos os números e termine com 0\n"))
 print("Existem",ímpar,"números impar e",par,"números pares")
main()