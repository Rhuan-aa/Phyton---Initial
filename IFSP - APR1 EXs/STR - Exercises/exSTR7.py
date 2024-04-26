f=input("Digite uma frase: ")
l=input("Digite uma letra que deseja eliminar todas as ocorrências: ")
nova_f=""

if l in f:
    for i in range(len(f)):
        if f[i]!=l or f[i]!=l:
            nova_f+=f[i]
    print(f"{nova_f}")

else:
    print("Não há ocorrência da letra na frase")
    
