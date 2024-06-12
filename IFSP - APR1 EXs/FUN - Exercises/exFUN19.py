#Função
def palindromo(s):
    pal=""
    palin=False
    for i in range(len(s)-1,-1,-1):
        pal+=s[i]
    
    if pal.upper()==s.upper():
        palin=True

    return palin

s=input("Digite uma palavra: ")
print(palindromo(s))
