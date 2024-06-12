def reorg(l):
    reorgl = []
    while l:  # Continua enquanto houver elementos na lista original
        menor_n = min(l)  # Encontra o menor elemento na lista
        reorgl.append(menor_n)  # Adiciona o menor elemento à lista reorganizada
        l.remove(menor_n)  # Remove o menor elemento da lista original
    return reorgl


# Programa Principal
lista=[]
n=int(input("Quantidade de numeros que deseja na lista: "))
for i in range(n):
    x=float(input("Digite um valor: "))
    lista.append(x)
print(f"A lista reorganizada de forma crescente é:")
print(reorg(lista))
                 
