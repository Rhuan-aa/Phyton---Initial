#Adicionar Contato ==========================
def add_con(dic):
    con=input("Digite o nome do contato que deseja adicionar: ")
    num=int(input("Digite o numero do contato: "))
    dic[con]={num}
    return dic

#Exibir Contato =============================
def exi_con(dic):
    con=input("Digite o nome do contato que deseja buscar: ")
    if con in dic.keys():
        print(dic.get(con))
    else:
        print("---* Contato não cadastrado *---")

#Excluir Contato ============================
def exc_con(dic):
    con=input("Digite o nome do contato que deseja excluir: ")
    del dic[con]
    return dic

#Alterar Contato ============================
def alt_con(dic):
    con=input("Digite o nome do contato que deseja excluir: ")
    if con in dic.keys():
        num=int(input("Digite o novo numero do contato: "))
        dic[con]=num
        return dic
    else:
        print("---* Contato não cadastrado *---")

##MENU ======================================
agenda={}
menu=True
while menu:
    print("\n\nAgenda Telefônica:\n")
    print("1 - Adicionar um Contato")
    print("2 - Exibir um Contato")
    print("3 - Excluir um Contato")
    print("4 - Alterar Contato")
    print("5 - Lista de Contatos")
    print("6 - Sair")
    opc=int(input("\nEscolha uma opção: "))
    if opc==1:
        agenda=add_con(agenda)
    elif opc==2:
        exi_con(agenda)
    elif opc==3:
        agenda=exc_con(agenda)
    elif opc==4:
        agenda=alt_con(agenda)
    elif opc==5:
        for con in agenda.keys():
            chave = con
            valor = agenda[con]
            print(f"{chave}:{valor}")
    elif opc==6:
        print("---* Encerrando Calculadora *---")
        menu=False
