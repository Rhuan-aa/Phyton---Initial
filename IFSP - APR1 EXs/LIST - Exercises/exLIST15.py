fra=[]
p=""
prim=True
novaf=""
while p != "fim":
    p=input("Digite algo: ")
    fra.append(p)

x=input("Escolha uma letra para tirar a primeira ocorrência de todas STRs: ")
for i in range(len(fra)):
    for d in range(len(fra[i])):
        if x!=fra[i][d]:
            novaf+=fra[i][d]
            fra[i]=novaf
        if x==fra[i][d] and prim==False:
            novaf+=fra[i][d]
            fra[i]=novaf
        if x==fra[i][d] and prim==True:
            prim=False
    prim=True
print(fra)

