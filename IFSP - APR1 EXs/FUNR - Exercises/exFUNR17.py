def inverter(s):
    if s=="":
        return ""
    if len(s)==1:
        return s
    else:
        return inverter(s[1:])+s[0]

def palindromo(s):
    p=False
    if s==inverter(s):
        p=True
    return p

#Programa Principal
string=input("Digite uma string: ")
print(palindromo(string))
