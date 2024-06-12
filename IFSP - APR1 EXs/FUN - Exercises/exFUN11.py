def potencia(b,e):
    r=b
    if e==0:
        r=1
    if e==1:
        r=b
    if e>0:
        for i in range(1,e):
            r*=b
    if e<0:
        for i in range(1,e):
            r*=b
        r=1/r
    return r

base=int(input("Digite a base que será utilizada na potencialização: "))
expoente=int(input("Digite o expoente que será utilizado na potencialização: "))
print(f"O resultado é {potencia(base,expoente)}")
