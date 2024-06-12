## O Arquivo Existe? ==============
def arq_exists(arq):
    import os
    if os.path.exists(arq):
        return True
    else:
        return False


### Ler Arquivo ===================
def arq_r(arq,dic):
    if arq_exists(arq):
        ref_arq=open(arq, "r")
        for linha in ref_arq:
            linha=linha[:len(linha)-1]
            aluno=linha.split("\b")
            nome=aluno[0]
            notas=[]
            for i in range(1,len(aluno)):
                nota=int(aluno[i])
                notas.append(nota)
            dic[nome]=notas
        ref_arq.close()
    else:
        print("Arquivo Inexistente!")

### Acima de 6 notas ==============
def student_plus6(dic):
    exists=False
    for aluno in dic.keys():
        nome=aluno
        if len(dic[aluno])>=6:
            print(f"{nome} | Notas: {dic[aluno]}")
            exists=True
    if exists==False:
        print("Não há alunos que possuem acima de 6 notas.")

### Média de Notas p/ Estudante =====
def students_grade_average(dic):
    for aluno in dic.keys():
        media=0
        for i in range(len(dic[aluno])):
            media+=dic[aluno][i]
        media=media/i
        print(f"{aluno} | {media}.")
### Nota Min / Max ==================
def min_max_grade(dic):
    maxgrade=0
    mingrade=0
    for aluno in dic.keys():
        maxgrade=max(dic[aluno])
        mingrade=min(dic[aluno])
        print("{aluno} | Nota max: {maxgrade} & Nota min: {mingrade}")


# Programa Principal ===============
dic_alunos={}
arq_r("estudantes.dat",dic_alunos)
menu=True
while menu:
    print("\n\nEX - ARQUIVO 5")
    print("\n1 - Acima de 6 notas")
    print("2 - Média das Notas")
    print("3 - Nota Min & Max")
    print("4 - Fim")
    op=int(input("\nEscolha uma opção: "))
    if op==1:
        print("\n")
        student_plus6(dic_alunos)
    if op==2:
        print("\n")
        students_grade_average(dic_alunos)
    if op==3:
        print("\n")
        min_max_grade(dic_alunos)
    if op==4:
        print("Finalizando Programa!!")
        menu=False
