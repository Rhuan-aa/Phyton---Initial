#Funções para reorganizar a lista
def reorg(l):
    reorgl = []
    while l:  
        maior_n = encontrar_n(l)  
        reorgl.append(maior_n)  
        l.remove(maior_n) 
    return reorgl

def encontrar_n(l):
    maior_n=float('-inf')
    for i in range(len(l)):
        if l[i]>maior_n:
            maior_n=l[i]
    return maior_n
        

# Programa Principal
lista=[]
n=int(input("Quantidade de numeros que deseja na lista: "))
for i in range(n):
    x=float(input("Digite um valor: "))
    lista.append(x)
print(f"A lista reorganizada de forma crescente é:")
print(reorg(lista))


##Programa feito tendo em vista as limitações dos códigos que podem ser utilizados.
