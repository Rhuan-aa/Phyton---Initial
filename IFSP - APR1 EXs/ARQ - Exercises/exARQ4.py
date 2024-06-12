### O Arquivo Existe? ==========================================================
def arq_exists(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False
    
### Gravar Arquivo =============================================================
def arqsave_alunos(arq,a):
    if len(a):
        ref_arq=open(arq,'w')
        for indice in a:
            chave=indice
            data, emails, disc = a[chave]
            linha = f"{chave[0]}" +"\t" + f"{chave[1]}" +"\t" + f"{data}" +"\t" 
            for i in range(len(emails)):
                linha+="*"
                linha+=f"{emails[i]}"
            linha+="\t"
            for i in range(len(disc)):
                linha+="#"
                linha+=f"{disc[i][0]}"
                linha+="&"
                linha+=f"{disc[i][1]}"            
            linha+="\n"
            ref_arq.write(linha)          
        ref_arq.close()
    else:
        print("Sem conteúdo para salvar!")

### Ler Arquivo ================================================================
def arqread_alunos(arq,a):
    if arq_exists(arq):
        ref_arq=open(arq,'r')
        for linha in ref_arq:
            linha=linha[:len(linha)-1]
            aluno = linha.split("\t") 
            RA=aluno[0]
            nome=aluno[1]
            data_nasc=aluno[2]
            emails = [aluno[3].split("*")]
            discs = [aluno[4].split("#")]
            disc = discs.split("&")
            a[(RA,nome)]=(data_nasc,[emails],[discs])
        ref_arq.close()
    else:
        print("Arquivo inexistente!")

## Programa Principal =========================
disciplinas={}
dic_alunos={}
arqread_alunos("cadastro.txt",dic_alunos)
menu=True
while menu:
    print("\n\nCRUD - IFSP")
    print("\n1 - Adicionar Aluno")
    print("2 - Alterar Aluno")
    print("3 - Remover Aluno")
    print("4 - Consultar um Aluno pela chave")
    print("5 - Mostrar todos os Alunos")
    print("6 - Adicionar disciplinas e notas ao Aluno")
    print("7 - Fim")
    op=int(input("\nEscolha uma opção: "))
    #Opção 1===================================
    if op==1:
        RA=input("\nDigite o RA do aluno: ")
        name=input("Digite o nome do aluno: ")
        data_nasc=input("Digite a data de nascimento do aluno no modelo DD/MM/AAAA: ")
        emails=[]
        q=int(input("Digite o numero de e-mails do aluno: "))
        for i in range(q):
            e=input("Digite o e-mail a ser adicionado: ")
            emails.append(e)
        chave=(RA,name)
        valor=(data_nasc,emails,[])
        dic_alunos[(chave)]=valor
        print(f"{name}:{dic_alunos.get(chave)}")
    #Opção 2=================================== ERRO
    if op==2:
        if dic_alunos!={}:
            RA=input("\n\nDigite o RA do aluno: ")
            name=input("Digite o nome do aluno: ")
            if (RA,name) in dic_alunos:
                print("\nDeseja alterar:")
                print("\n1 - Data de Nascimento")
                print("2 - E-mails")
                print("3 - Ambos")
                opc=int(input("\nEscolha uma opção: "))
                chave=(RA,name)
                   
                if opc==1:
                    data_nasc=input("Digite a nova data de nascimento no modelo DD/MM/AAAA: ")
                    valor=(data_nasc,dic_alunos[(chave)][1],dic_alunos[(chave)][2])
                    dic_alunos[(chave)]=valor
                    print(f"{name}:{dic_alunos.get(chave)}")
                        
                if opc==2:
                    emails=[]
                    q=int(input("Digite o novo numero de e-mails do aluno: "))
                    for i in range(q):
                        e=input("Digite o e-mail a ser adicionado: ")
                        emails.append(e)
                    valor=(dic_alunos[(chave)][0],emails,dic_alunos[(chave)][2])
                    dic_alunos[(chave)]=valor
                    print(f"{name}:{dic_alunos.get(chave)}")
                    
                if opc==3:
                    data_nasc=input("Digite a nova data de nascimento no modelo DD/MM/AAAA: ")
                    emails=[]
                    q=int(input("Digite o novo numero de e-mails do aluno: "))
                    for i in range(q):
                        e=input("Digite o e-mail a ser adicionado: ")
                        emails.append(e)
                    valor=(data_nasc,emails,dic_alunos[(chave)][2])
                    dic_alunos[(chave)]=valor
                    print(f"{name}:{dic_alunos.get(chave)}")
            else:
                print("Esse aluno não está registrado no sistema")
        else:
            print("Não possui alunos a serem alterados.")
    #Opção 3===================================
    if op==3:
        if dic_alunos!={}:
            RA=input("\n\nDigite o RA do aluno: ")
            name=input("Digite o nome do aluno: ")
            if (RA,name) in dic_alunos:
                del dic_alunos[(RA,name)]
                print(f"Aluno {name} retirado do sistema")
            else:
                print("Esse aluno não está registrado no sistema")
        else:
            print("Não possui alunos a serem retirados.")
    #Opção 4===================================
    if op==4:
        if dic_alunos!={}:
            RA=input("\n\nDigite o RA do aluno: ")
            name=input("Digite o nome do aluno: ")
            if (RA,name) in dic_alunos:
                print(f"\nAluno: {name} | RA: {RA}")
                print(f"Data de Nascimento:  {dic_alunos[(RA,name)][0]}")
                print(f"E-mails:  {dic_alunos[(RA,name)][1]}")
                print(f"Disciplinas | Notas: {dic_alunos[(RA,name)][2]}")
            else:
                print("Esse aluno não está registrado no sistema")
        else:
            print("Não possui alunos a serem consultados.")
    #Opção 5===================================
    if op==5:
        if dic_alunos!={}:
            print("\nLista de Alunos:")
            for i in dic_alunos.keys():
                print(f"{i[1]}")
        else:
            print("Não possui alunos a serem mostrados.")
    #Opção 6===================================
    if op==6:
        if dic_alunos!={}:
            RA=input("\n\nDigite o RA do aluno: ")
            name=input("Digite o nome do aluno: ")
            if (RA,name) in dic_alunos:
                s=input("\nDigite sigla da disciplina que deseja adicionar ao aluno: ")
                if s not in disciplinas:
                    d=input("Essa disciplina não existe no sistema, deseja cadastrar? (Sim ou Não)")
                    if d=="Sim":
                        n=input("Digite o nome da disciplina")
                        ch=int(input("Digite a carga horária da disciplina: "))
                if d!="Não":
                    no=int(input("Digite a nota do aluno na diciplina: "))
                    disciplinas[s]=[n,ch]
                    data, emails, discs = dic_alunos[(RA,name)]
                    disc=[s,no]
                    discs.append(disc)
                    dic_alunos[(RA,name)]=(data,[emails],[discs])
            else:
                print("Esse aluno não está registrado no sistema")
        else:
            print("Não possui alunos a serem consultados.")
    #Opção 7===================================
    if op==7:
        print("--Programa Encerrado--")
        arqsave_alunos("cadastro.txt",dic_alunos)
        menu=False
        
