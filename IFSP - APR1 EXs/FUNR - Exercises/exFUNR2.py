def pot(x, y):
    if y==0:
        return 1
    else:
        return x*pot(x, y-1)

num=int(input('Digite um numero: '))
exp=int(input("Digite um expoente: "))
resultado=pot(num, exp)
print(f"O resultado da potência foi {resultado}")
