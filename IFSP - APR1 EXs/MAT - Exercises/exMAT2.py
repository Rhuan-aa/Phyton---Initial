#linhas:
M=int(input("Digite o numero de linhas: "))

#colunas:
N=int(input("Digite o numero de colunas: "))

mat=[]
for i in range(M):
    linha=[]
    for j in range(N):
        x=int(input(f"Informe o valor contido na posição [{i}][{j}]: "))
        linha.append(x)
    mat.append(linha)

print("Matriz escrita em forma matricial: ")
for i in range(M):
    for j in range(N):
        print(mat[i][j], end=' ')
    print()
