#Função para media de uma lista de numeros reais
def media(l):
    media=0
    div=0
    for i in l:
        media+=i
        div+=1
    media=media/div
    return media

# Programa Principal
lista=[]
n=int(input("Quantidade de numeros que deseja na lista: "))
for i in range(n):
    x=float(input("Digite um valor: "))
    lista.append(x)
print(f"A media da lista é {media(lista)}")
