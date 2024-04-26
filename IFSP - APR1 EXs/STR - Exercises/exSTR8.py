f=input("Digite uma frase: ")
l=input("Digite uma letra que deseja verificar o numero de ocorrências: ")
num=0
if l in f:
    for i in range(len(f)):
        if f[i]==l:
            num+=1
    print(f"O numero de ocorrências da letra escolhida é {num}")

else:
    print("Não há ocorrência da letra na frase")
