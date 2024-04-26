f=input("Digite uma frase: ")
l=input("Digite a letra que deseja apagar a ultima ocorrência: ")
r=False
posicao=-1
nova_f=""

for i in range(len(f)-1,-1,-1):
    if f[i]==l and r==False:
        posicao=i
        r=True
        
if posicao!=-1:
    nova_f=f[:posicao] + f[posicao+1:]
else:
    nova_frase = "A letra não foi encontrada na frase."
print(f"{nova_f}")

