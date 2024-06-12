linhas=3
colunas=3
somat=0
somal=0
mat=[]

for i in range(linhas):
    linha=[]
    for j in range(colunas):
        x=int(input(f"Informe o numero que deseja colocar na posição [{i}][{j}]: "))
        linha.append(x)
        somat+=x
    mat.append(linha)

print("Matriz escrita em forma matricial: ")
for i in range(linhas):
    for j in range(colunas):
        print(mat[i][j], end=' ')
    print()
print(f"A soma de todos elementos da matriz é {somat}")

for i in range(linhas):
    somal=0
    for j in range(colunas):
        somal+=j
    print(f"A soma da linha [{i}] é igual a {somal}")
