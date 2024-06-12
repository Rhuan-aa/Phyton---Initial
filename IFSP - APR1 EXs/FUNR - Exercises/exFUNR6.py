def exibir_verticalmente(string):
    if len(string) == 0:
        return
    else:
        print(string[0])
        exibir_verticalmente(string[1:])
        
fra=input("Digite uma string: ")
print(exibir_verticalmente(fra))
