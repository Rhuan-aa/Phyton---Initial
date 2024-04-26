n=int(input("Digite a quantidade de numeros que irão entrar na lista: "))
lista=[]
for i in range(n):
    q=int(input("Digite o numero que irá entrar na lista: "))
    lista.append(q)
x=int(input("Digite um numero que deseja saber se existe dentro da lista: "))
if x in lista:
    print("O numero existe dentro da lista.")
else:
    print("O numero não existe dentro da lista.")
