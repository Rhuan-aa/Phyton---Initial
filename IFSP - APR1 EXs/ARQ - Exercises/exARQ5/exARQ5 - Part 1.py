###Salvar arquivo ============================
def arq_w(arq,dic):
    ref_arq=open(arq, "w")
    for aluno in dic:
        chave = aluno
        notas = dic_alunos[chave]
        linha= f"{aluno}" 
        for i in range(len(notas)):
            linha+= "\b"
            linha+=f"{notas[i]}"
        linha+="\n"
        ref_arq.write(linha)
    ref_arq.close()
    print("Arquivo salvo com sucesso!!!")
 

## Programa Principal ========================
dic_alunos={}

stop=False
while stop==False:
    print("\n1 - Adicionar Aluno")
    print("2 - Parar Programa")
    opc=int(input("\nDigite uma opção:"))
    if opc==1:
        alu=input("Digite o nome do aluno: ")
        notas=[]
        num=int(input("Digite o numero de notas: "))
        for i in range(num):
            no=int(input("Digite a nota: "))
            notas.append(no)
        dic_alunos[alu]=notas
    if opc==2:
        stop=True
        print("Programa encerrado!!")
arq_w("estudantes.dat",dic_alunos)
