def contador(a, lista):
    count=0
    if len(lista) == 0:
        return 0
    c=contador(a, lista[1:])
    if lista[0]==a:
        count+=1
    return count

q=int(input("Quantos elementos tem a lista: "))
lista=[]
for i in range(q):
    x=int(input("Digite o valor a ser alocado na lista: "))
    lista.append(x)
v=int(input("Qual valor que deve ser procurado: "))
print(f"O numero de vezes que {v} aparece na lista é: {contador(v, lista)}")
