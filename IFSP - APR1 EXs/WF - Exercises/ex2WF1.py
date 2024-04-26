n1=int(input("Digite um numero inteiro: "))
n2=int(input("Digite outro numero inteiro: "))

if n1>n2:
    for i in range(n1, n2-1,-1):
        print(i)
elif n1<n2:
    for i in range(n2, n1-1,-1):
        print(i)
else:
    print("Não exitem numeros inteiros entre esses numeros")

