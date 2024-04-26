nome=input("Digite seu nome: ")

for n in range(len(nome)):
    print(f"{nome[:len(nome)-n]}")
