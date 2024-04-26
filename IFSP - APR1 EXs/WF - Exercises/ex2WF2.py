b=int(input("Digite um numero inteiro: "))
exp=int(input("Digite um numero inteiro >=0: "))
resul=b
for i in range(0, exp-1):
    resul=resul*b
if exp==0:
    resul=1
print(resul)
