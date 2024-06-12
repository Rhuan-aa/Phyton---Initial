### Dados ======================================================================
produtos={}

### O Arquivo Existe? ==========================================================
def arq_exists(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

### Adicionando ao Estoque =====================================================
def addstorage(p):
    cod=int(input("\nDigite o código do produto: "))
    if cod in produtos.keys():
        print("Error: código de produto já existente")
    else:
        item=input("Informe o nome do produto: ")
        custo=float(input("Informe o preço do produto: "))
        quant=int(input("Informe a quantidade do produto em estoque: "))
        p[cod]=[item,(custo,quant)]

### Venda ======================================================================
def sellitem(p,cod,sell):
    if cod not in p.keys():
        print("Produto não encontrado")
    else:
        item, status = p[cod]
        if sell>status[1]:
            return print("Impossível realizar a venda")
        else:
            quant=status[1]-sell
            venda=status[0]*sell
            p[cod]=[item,(status[0],quant)]
            return venda

### Estoque Mínimo =============================================================
def minstorage(p,num):
    search=False
    for i in p.keys():
        cod=i
        item, status = p[cod]
        if status[1]<=num:
            print(f"{item}: R${status[0]} | {status[1]} unidades.")
            search=True
    if search==False:
        print("Nenhum produto encontrado!")

### Alterar Preço ==============================================================
def altprice(p,cod,num):
    if cod not in p.keys():
        print("Produto não encontrado")
    else:
        item, status = p[cod]
        p[cod]=[item,(num,status[1])]

### Ler Arquivo ================================================================
def arqread(arq,p):
    if arq_exists(arq):
        ref_arq=open(arq,'r')
        for linha in ref_arq:
            linha=linha[:len(linha)-1] #removendo o '\n'
            produto = linha.split("\t") #quebra no mesmo separador
            código=int(produto[0])
            item=produto[1]
            preço=float(produto[2])
            quant=int(produto[3])
            p[código]=[item,(preço,quant)]
        ref_arq.close()
    else:
        print("Arquivo inexistente!")


### Gravar Arquivo =============================================================
def arqsave(arq,p):
    if len(p):
        ref_arq=open("estoque.txt",'w')
        for indice in produtos:
            chave=indice
            item, status = produtos[chave]
            linha = f"{chave}" +"\t" + f"{item}"+ "\t" + f"{status[0]}" + "\t" + f"{status[1]}" + "\n"
            ref_arq.write(linha)
        ref_arq.close()
    else:
        print("Sem conteúdo para salvar!")

### Programa principal =========================================================
on=True
arqread("estoque.txt",produtos)
while on==True:
    ### MENU ===================================================================
    print("\n\nPrograma de Estoque:\n")
    print("1 - Inserir Produto")
    print("2 - Efetuar Venda")
    print("3 - Exibir produtos de estoque mínimo")
    print("4 - Alterar preço de um produto")
    print("5 - Mostrar todos os produtos")
    print("6 - Sair")
    opc=int(input("\nEscolha uma opção: "))
    ## Opção 1 =================================================================
    if opc==1:
        add=addstorage(produtos)
    ## Opção 2 =================================================================
    if opc==2:
        cod=int(input("\nDigite o código do produto: "))
        sell=int(input("digite a quantidade vendida: "))
        custo=sellitem(produtos,cod,sell)
        print(f"O valor da venda foi R${custo}")
    ## Opção 3 =================================================================
    if opc==3:
        val=int(input("\nDigite até qual quantidade os itens devem possuir: "))
        minstorage(produtos,val)
    ## Opção 4 =================================================================
    if opc==4:
        cod=int(input("\nDigite o código do item que deseja alterar: "))
        val=float(input("Digite o novo preço do item: "))
        altprice(produtos,cod,val)
    ## Opção 5 =================================================================
    if opc==5:
        print()
        for i in produtos.keys():
            item, status = produtos[i]
            print(f"{item}: R${status[0]} | {status[1]} unidades.")
    ## Opção 6 =================================================================
    if opc==6:
        arqsave("estoque.txt",produtos)
        on=False
        print("=== PROGRAMA ENCERRADO ===")
