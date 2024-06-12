def multiplicação(lista):
    if len(lista)==0:
        return 0
    if len(lista)==1:
        return lista[0]
    return lista[0]*multiplicação(lista[1:])

#Programa Principal
q=int(input("Quantidade de numeros terá na lista: "))
lista=[]
for i in range(q):
    x=int(input("Digite um valor que deseja alocar na lista: "))
    lista.append(x)
print(multiplicação(lista))
