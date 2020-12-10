x = int(input("Escolha\n1.Cagar\n2.Mijar\n3.Peidar\n"))

if x == 1:
    print("cagão")
else:
    print("mijão")

x = 10
y = 15
z = 25
print(x == z - y and z != y - x or not y != z - x)
