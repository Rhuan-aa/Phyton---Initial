#Função
def mult(l):
    mult=1
    for i in l:
        mult*=i
    return mult

# Programa Principal
lista=[]
n=int(input("Quantidade de numeros que deseja na lista: "))
for i in range(n):
    x=float(input("Digite um valor: "))
    lista.append(x)
print(f"O produto desses numeros é {mult(lista)}")
