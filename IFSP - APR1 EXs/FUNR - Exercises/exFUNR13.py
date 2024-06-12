def contar(lista, x):
    if len(lista)==0:
        return 0
    if lista[0]==x:
        return 1+contar(lista[1:],x)
    else:
        return 0+contar(lista[1:],x)

#Programa Principal
q=int(input("Quantidade de numeros terá na lista: "))
lista=[]
for i in range(q):
    z=int(input("Digite um valor que deseja alocar na lista: "))
    lista.append(z)
n=int(input("Numero que deve ser contado: "))
print(contar(lista, n))
