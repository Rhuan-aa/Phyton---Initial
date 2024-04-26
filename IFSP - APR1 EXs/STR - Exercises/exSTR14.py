sequencia=input("Digite uma sequência de letras: ")
subsequencia_atual = sequencia[0]
sequencias_iguais = ""

for i in range(1, len(sequencia)):
    if sequencia[i] == sequencia[i - 1]:
        subsequencia_atual += sequencia[i]
    else:
        print(subsequencia_atual)
        subsequencia_atual = sequencia[i]
print(subsequencia_atual)
