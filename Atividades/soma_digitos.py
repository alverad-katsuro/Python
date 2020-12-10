def main():
 n = (input("Digite o número que deseja somar: "))
 f = int(len(n))
 z = 0
 x = 0
 while x < f+1:
  n = int(n)
  if (n / 10 != 0):
   z = z + (n % 10)
   n = (n//10)
   x = x+1
  else:
   x = x+1
 print (z)
main()
