n=int(input("Digite um valor: "))
lista=[]
ultimo=True

for i in range(n):
    x=int(input("Digite um numero: "))
    lista.append(x)

r=int(input("Digite o numero que deve ser retirado em sua ultima ocorrência: "))
for i in range(len(lista)-1,-1,-1):
    if lista[i]==r and ultimo==True:
        ultimo=False
        del lista[i]
print(lista)
