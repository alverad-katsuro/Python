def main():
	x = int(input("Digite um número para saber se ele é divisivel por 5 ou por 3\n"))
	if x % 3 == 0 and x % 5 == 0:
	 print ("FizzBuzz")
	else:
	 print (x)
main()