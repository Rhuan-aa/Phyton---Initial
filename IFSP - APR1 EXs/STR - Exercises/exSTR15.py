palavra=input("Digite um palavra: ")
p1=""
p2=""

for i in range(len(palavra)):
    p1+=palavra[i]

for r in range(len(palavra)-1,-1,-1):
    p2+=palavra[r]

if p1==p2:
    print("Sim")
else:
    print("Não")
