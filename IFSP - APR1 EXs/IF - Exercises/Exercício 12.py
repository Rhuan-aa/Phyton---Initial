p=int(input("Qual posição está a porta P:"))
r=int(input("Qual posição está a porta R:"))


if p==0 and r>=0:
    print("A bolinha saiu pelo caminho C")
elif p==1 and r==0:
    print("A bolinha saiu pelo caminho B")
else:
    print("A bolinha saiu pelo caminho A")
