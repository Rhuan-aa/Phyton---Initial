frase=input("Digite uma frase: ")
numero="0123456789"
barra="/"
dia=""
mês=""
ano=""
diae=False


for i in range(len(frase)):
    if frase[i] in numero and frase[i+1] in numero and frase[i+2] in barra:
        print(f"Dia:{frase[i]}{frase[i+1]}")
        diae=True
    if frase[i] in numero and frase[i+1] in numero and frase[i+2] in barra and diae==True:
        print(f"Mês:{frase[i]}{frase[i+1]}")
        diae=False
    if frase[i] in numero and frase[i+1] in numero and frase[i+2] in numero and frase[i+3] in numero and frase[i-1] in barra:
        print(f":{frase[i]}{frase[i+1]}{frase[i+2]}{frase[i+3]}")
