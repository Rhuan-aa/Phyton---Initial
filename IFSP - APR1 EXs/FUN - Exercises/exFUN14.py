#Função
def analise(l):
    maior_n=float('-inf')
    for i in range(len(l)):
        if l[i]>maior_n:
            maior_n=l[i]
    return maior_n

# Programa Principal
lista=[]
posi=0
n=int(input("Quantidade de numeros que deseja na lista: "))
for i in range(n):
    x=float(input("Digite um valor: "))
    lista.append(x)
for i in range(len(lista)):
    if lista[i]==analise(lista):
        posi=i
    
print(f"O maior numero da lista é {analise(lista)} e sua posição {posi}")
