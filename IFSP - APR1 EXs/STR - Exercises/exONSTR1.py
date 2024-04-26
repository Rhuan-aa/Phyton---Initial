f1=input("Digite uma frase: ")
f2=input("Digite outra frase: ")

print(f"A primeira frase possui {len(f1)} carácteres.")
print(f"A segunda frase possui {len(f2)} carácteres.")

if len(f1)==len(f2):
    print("O numero de caracteres de ambas as frases é igual.")
else:
    print("O numero de caracteres das frases é diferente.")
    
if f1==f2:
    print("O conteúdo das frases é igual.")
else:
    print("O conteúdo das frases é diferente.")
