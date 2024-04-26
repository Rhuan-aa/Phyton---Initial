N=int(input("Digite a quantia de numeros na lista: "))
lista=[]
lista2=[]
y=0
for i in range(N):
    X=int(input("Digite um numero: "))
    lista.append(X)

for i in range(N-1,-1,-1):
    y=lista[i]
    lista2.append(y)
print(lista2)
