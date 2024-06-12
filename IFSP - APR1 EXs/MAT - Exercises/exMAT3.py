mat=[]
diag=[]
valt=0

lc=int(input("Digite o numero de linhas e colunas da matriz quadrada: "))

for i in range(lc):
    linha=[]
    for j in range(lc):
        x=int(input(f"Digite o valor que será integrado na posição [{i}][{j}]: "))
        linha.append(x)
    mat.append(linha)

for i in range(lc):
    linha=[]
    for j in range(lc):
        x=" "
        linha.append(x)
    diag.append(linha)

for i in range(lc):
    for j in range(lc):
        diag[i][i]=mat[i][i]
    valt+=mat[i][i]
    
print("Matriz escrita em forma matricial: ")
for i in range(lc):
    for j in range(lc):
        print(mat[i][j], end=' ')
    print()

print("Sua diagonal escrita em forma matricial: ")
for i in range(lc):
    for j in range(lc):
        print(diag[i][j], end=' ')
    print()
print(f"Tendo valor de {valt}")
