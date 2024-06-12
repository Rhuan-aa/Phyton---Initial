def eliminar(s, x):
    if s=="":
        return ""
    elif s[0]==x:
        return eliminar(s[1:], x)
    else:
        return s[0]+eliminar(s[1:], x)

#Programa Principal
string=input("Digite uma string: ")
l=input("Elemento que deve ser retirado: ")
print(eliminar(string, l))
