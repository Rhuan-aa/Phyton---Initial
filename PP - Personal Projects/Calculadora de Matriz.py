#Soma de Matrizes
def somamat(mat,mat2,i,j):
    mat3=[]
    for k in range(i):
        linha=[]
        for l in range(j):
            x=mat[k][l]+mat2[k][l]
            linha.append(x)
        mat3.append(linha)
    return mat3
        
#Subtração de Matrizes
def submat(mat,mat2,i,j):
    mat3=[]
    for k in range(i):
        linha=[]
        for l in range(j):
            x=mat[k][l]-mat2[k][l]
            linha.append(x)
        mat3.append(linha)
    return mat3

#Matriz Indentidade
def idenmat(i,j):
    if i==j:
        mati=[]
        for k in range(i):
            linha=[]
            for l in range(j):
                if k==l:
                    x=1
                else:
                    x=0
                linha.append(x)
            mati.append(linha)
        return mati
    else:
        return print("Não cumpre os requisitos.")



#Matriz Simétrica
def simmat(mat,i,j):
    if mat==transmat(mat,i,j):
        return print("Sim, se trata de uma matriz simétrica.")
    else:
        return print("Não, não se trata de uma matriz simétrica.")

#Diagonal Principal
def diagp(mat,t):
    diag = []
    for i in range(t):
        linha = []
        for j in range(t):
            if i == j:
                linha.append(mat[i][j])
            else:
                linha.append(0)
        diag.append(linha)
    return diag

#Diagonal Secundária
def diags(mat,t):
    diag=[]
    for i in range(t):
        linha=[]
        for j in range(t):
            if i+j == t-1:
                linha.append(mat[i][j])
            else:
                linha.append(0)
        diag.append(linha)
    return diag

#Multiplicação de Matrizes
def multmat(mat,mat2,i,j,i2,j2):
    if j==i2:
        mat3=[]
        for k in range(i):
            linha=[]
            for l in range(j2):
                x=0
                for z in range(j):
                    x+=mat[k][z]*mat2[z][l]
                linha.append(x)
            mat3.append(linha)
        return mat3
    else:
        return print("Não cumpre os requisitos.")

#Traço
def traço(mat,i):
    mat=diagp(mat,i)
    soma=0
    for l in range(i):
        for k in range(i):
            soma+=diagp(mat,i)[l][k]
    return soma

#Matriz Transposta
def transmat(mat,i,j):
    matt=[]
    for k in range(j):
            linha=[]
            for l in range(i):
                x=mat[l][k]
                linha.append(x)
            matt.append(linha)
    return matt

#Determinante da Matriz
def obter_subdet(mat, p, q, n):
    dmat = []
    for k in range(n):
        linha = []
        for l in range(n):
            if k != p and l != q:
                linha.append(mat[k][l])
        if linha:
            dmat.append(linha)
    return dmat

def detmat(mat, n):
    if n == 1:
        return mat[0][0]
    if n == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    det = 0
    sinal = 1
    for f in range(n):
        subdet = obter_subdet(mat, 0, f, n)
        det += (sinal * mat[0][f] * detmat(subdet, n - 1))
        sinal = -sinal
    return det
    
###MENU==================================================
def menu():
    menu=print("\n\nCalculadora de Matrizes:\n", "1 - Soma de Matrizes\n", "2 - Subtração de Matrizes\n", "3 - Multiplicação de Matrizes\n", "4 - A Matriz é simétrica?\n", "5 - Transposição de Matriz\n", "6 - Diagonal Principal de uma Matriz\n", "7 - Diagonal Secundária de uma Matriz\n" , "8 - Traço de uma Matriz\n", "9 - Matriz Identidade\n", "10 - Determinante da Matriz\n")
    op=int(input("\nSelecione a opção a partir do numero: "))
    #Opção 1 ============================================
    if op==1:
        print("\nDEVEM SER DUAS MATRIZES DE MESMA ORDEM")
        print("\nPara as Matrizes")
        linhas=int(input("Digite o numero de linhas delas: "))
        colunas=int(input("Digite o numero de colunas delas: "))
        mat=[]
        print("\n\nPara a Primeira Matriz:")
        for i in range(linhas):
            linha=[]
            for j in range(colunas):
                x=int(input(f"Digite o valor do elemento {[i]}{[j]}: "))
                linha.append(x)
            mat.append(linha)
        mat2=[]
        print("\nPara a Segunda Matriz:")
        for i in range(linhas):
            linha=[]
            for j in range(colunas):
                x=int(input(f"Digite o valor do elemento {[i]}{[j]}: "))
                linha.append(x)
            mat2.append(linha)
        print("\nMATRIZ APÓS A SOMA:")
        for i in range(linhas):
            for j in range(colunas):
                print(somamat(mat,mat2,linhas,colunas)[i][j], end=" ")
            print()
    #Opção 2 ============================================
    if op==2:
        print("\nDEVEM SER DUAS MATRIZES DE MESMA ORDEM")
        print("\nPara as Matrizes")
        linhas=int(input("Digite o numero de linhas delas: "))
        colunas=int(input("Digite o numero de colunas delas: "))
        mat=[]
        print("\n\nPara a Primeira Matriz:\n")
        for i in range(linhas):
            linha=[]
            for j in range(colunas):
                x=int(input(f"Digite o valor do elemento {[i]}{[j]}: "))
                linha.append(x)
            mat.append(linha)
        mat2=[]
        print("\nPara a Segunda Matriz:\n")
        for i in range(linhas):
            linha=[]
            for j in range(colunas):
                x=int(input(f"Digite o valor do elemento {[i]}{[j]}: "))
                linha.append(x)
            mat2.append(linha)
        print("\nMATRIZ APÓS A SUBTRAÇÃO:\n")
        for i in range(linhas):
            for j in range(colunas):
                print(submat(mat,mat2,linhas,colunas)[i][j], end=" ")
            print()
    #Opção 3 ============================================
    if op==3:
        print("\nA MATRIZ 2 DEVE TER UM NUMERO DE LINHAS IGUAL A QUE A PRIMEIRA TEM DE COLUNAS")
        print("\n\nPara a Primeira Matriz:\n")
        linhas=int(input("Digite o numero de linhas da matriz: "))
        colunas=int(input("Digite o numero de colunas da matriz: "))
        mat=[]
        for i in range(linhas):
            linha=[]
            for j in range(colunas):
                x=int(input(f"Digite o valor do elemento {[i]}{[j]}: "))
                linha.append(x)
            mat.append(linha)
        print("\nPara a Segunda Matriz:\n")
        mat2=[]
        linhas2=int(input("Digite o numero de linhas da matriz: "))
        colunas2=int(input("Digite o numero de colunas da matriz: "))
        for i in range(linhas2):
            linha=[]
            for j in range(colunas2):
                x=int(input(f"Digite o valor do elemento {[i]}{[j]}: "))
                linha.append(x)
            mat2.append(linha)
        print("\nMATRIZ APÓS A MULTIPLICAÇÃO::\n")
        for i in range(linhas):
            for j in range(colunas):
                print(multmat(mat,mat2,linhas,colunas,linhas2,colunas2)[i][j], end=" ")
            print()
    #Opção 4 ============================================
    if op==4:
        print("\nDIGITE UMA MATRIZ PARA SABER SE ELA É SIMÉTRICA OU NÃO")
        linhas=int(input("Digite o numero de linhas da matriz: "))
        colunas=int(input("Digite o numero de colunas da matriz: "))
        mat=[]
        for i in range(linhas):
            linha=[]
            for j in range(colunas):
                x=int(input(f"Digite o valor do elemento {[i]}{[j]}: "))
                linha.append(x)
            mat.append(linha)
        print(simmat(mat,linhas,colunas))
    #Opção 5 ============================================
    if op==5:
        print("\nDIGITE UMA MATRIZ PARA SER TRANSPOSTA")
        linhas=int(input("Digite o numero de linhas da matriz: "))
        colunas=int(input("Digite o numero de colunas da matriz: "))
        mat=[]
        for i in range(linhas):
            linha=[]
            for j in range(colunas):
                x=int(input(f"Digite o valor do elemento {[i]}{[j]}: "))
                linha.append(x)
            mat.append(linha)
        for i in range(colunas):
            for j in range(linhas):
                print(transmat(mat,linhas,colunas)[i][j], end=" ")
            print()
    #Opção 6 ============================================
    if op==6:
        print("\nDEVE SER UMA MATRIZ QUADRADA")
        print("\nPara a Matriz:")
        linhas=int(input("Digite o numero de linhas e colunas da matriz: "))
        colunas=linhas
        mat=[]
        for i in range(linhas):
            linha=[]
            for j in range(colunas):
                x=int(input(f"Digite o valor do elemento {[i]}{[j]}: "))
                linha.append(x)
            mat.append(linha)
        for i in range(linhas):
            for j in range(colunas):
                print(diagp(mat,linhas)[i][j], end=" ")
            print()
    #Opção 7 ============================================
    if op==7:
        print("\nDEVE SER UMA MATRIZ QUADRADA")
        print("\nPara a Matriz:")
        linhas=int(input("Digite o numero de linhas e colunas da matriz: "))
        colunas=linhas
        mat=[]
        for i in range(linhas):
            linha=[]
            for j in range(colunas):
                x=int(input(f"Digite o valor do elemento {[i]}{[j]}: "))
                linha.append(x)
            mat.append(linha)
        for i in range(linhas):
            for j in range(colunas):
                print(diags(mat,linhas)[i][j], end=" ")
            print()
    #Opção 8 ============================================
    if op==8:
        print("\nDEVE SER UMA MATRIZ QUADRADA")
        print("\nPara a Matriz:")
        linhas=int(input("Digite a Ordem da Matriz Identidade: "))
        colunas=linhas
        mat=[]
        for i in range(linhas):
            linha=[]
            for j in range(colunas):
                x=int(input(f"Digite o valor do elemento {[i]}{[j]}: "))
                linha.append(x)
            mat.append(linha)
        print(f"{traço(mat,linhas)} é o valor do traço")
    #Opção 9 ============================================
    if op==9:
        print("\nDEVE SER UMA MATRIZ QUADRADA")
        print("\nPara a Matriz:")
        linhas=int(input("Digite o numero de linhas e colunas da matriz: "))
        colunas=linhas
        for i in range(linhas):
            for j in range(colunas):
                print(idenmat(linhas,colunas)[i][j], end=" ")
            print()
    #Opção 10 ============================================
    if op==10:
        print("\nDEVE SER UMA MATRIZ QUADRADA")
        print("\nPara a Matriz:")
        linhas=int(input("Digite a Ordem da Matriz: "))
        colunas=linhas
        mat=[]
        for i in range(linhas):
            linha=[]
            for j in range(colunas):
                x=int(input(f"Digite o valor do elemento {[i]}{[j]}: "))
                linha.append(x)
            mat.append(linha)
        print(f"A determinante é {detmat(mat, linhas)}")
        
on=True
while on==True:
    menu()
