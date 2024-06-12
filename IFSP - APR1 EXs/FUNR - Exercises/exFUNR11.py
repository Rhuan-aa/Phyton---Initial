def retirar(lista):
    if len(lista)==0:
        return []
    else:
        if lista[0]%2==0:
            return retirar(lista[1:])
        else:
            return [lista[0]] + retirar(lista[1:])

q=int(input("Quantos elementos tem a lista: "))
lista=[]
for i in range(q):
    x=int(input("Digite o valor a ser alocado na lista: "))
    lista.append(x)
print(retirar(lista))
