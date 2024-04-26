nome=input("Digite um nome: ")
rnome=""

for i in range(len(nome)-1,-1,-1):
    rnome+=nome[i]
print(f"{rnome.upper()}")
