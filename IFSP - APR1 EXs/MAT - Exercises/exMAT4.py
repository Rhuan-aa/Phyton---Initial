diag=[]

lc=int(input("Digite o numero de linhas e colunas da matriz quadrada: "))

for i in range(lc):
    linha=[]
    for j in range(lc):
        x=0
        linha.append(x)
    diag.append(linha)

for i in range(lc):
    for j in range(lc):
        diag[i][i]=1
    
print("Matriz identidade: ")
for i in range(lc):
    for j in range(lc):
        print(diag[i][j], end=' ')
    print()

