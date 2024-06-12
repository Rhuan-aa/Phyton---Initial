def inverter(s):
    if s=="":
        return ""
    if len(s)==1:
        return s
    else:
        return inverter(s[1:])+s[0]

#Programa Principal
string=input("Digite uma string: ")
print(inverter(string))
