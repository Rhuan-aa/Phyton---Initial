#Função
def soma(l):
    soma=0
    for i in l:
        soma+=i
    return soma

# Programa Principal
lista=[]
n=int(input("Quantidade de numeros que deseja na lista: "))
for i in range(n):
    x=float(input("Digite um valor: "))
    lista.append(x)
print(f"A soma desses numeros é {soma(lista)}")
