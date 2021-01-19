## delta < 0 = nao tem raiz =0 1 raiz , delta > 0 =2 raiz
def main():
 import math
 print("A seguir calcularemos equações de 2º Grau\nLembrado que a formula geral é\nax**2+bx+c=0")
 a = float(input("Insira o valor de a: "))
 b = float(input("Insira o valor de b: "))
 c = float(input("Insira o valor de c: "))
 d = ((b**2) - (4*a*c))
 if d > 0 or d == 0:
  raiz = math.sqrt(d)
  if d > 0 and type(d) == float:
   x1 = ((-b) + raiz) / (2 * a)
   x2 = ((-b) - raiz) / (2 * a)
   print("O valor das raizes é\nx1 =",x1,"\nx2 =",x2)
  else:
   x1 = ((-b) + raiz) / (2 * a)
   print("Só há uma raiz x1 =",x1)
 else:
   print("Não há raiz")
main()