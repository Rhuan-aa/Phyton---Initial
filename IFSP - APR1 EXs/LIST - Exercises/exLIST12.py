N=int(input("Digite um valor: "))
lista=[]
primeiro=True
t=0

for i in range(N):
    X=int(input("Digite um numero: "))
    lista.append(X)

R=int(input("Digite o numero que deseja retirar a primeira ocorrência:"))
for i in lista:
    if i==R and primeiro==True:
        del lista[t]
        primeiro=False
    t+=1
print(lista)
