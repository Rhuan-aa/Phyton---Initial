f=input("Digite um frase: ")
vazio=" "
vogais="aeiouAEIOU"
nvog=0
nvaz=0

for i in range(len(f)):
    if f[i] in vogais:
        nvog+=1
    if f[i] in vazio:
        nvaz+=1
print(f"O numero de vogais é {nvog} e de Espaços Vazios é {nvaz}")
