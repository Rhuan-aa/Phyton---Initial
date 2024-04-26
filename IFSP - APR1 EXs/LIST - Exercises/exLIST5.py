A=[]
si=0
sp=0
for i in range(15):
    n=int(input("Digite um numero: "))
    if n%2==0 or n==0:
        sp+=n
    if n%2!=0:
        si+=n
    A.append(n)

print(f"Dentro da lista A({A})")
print(f"A soma dos numeros pares é {sp}, ja dos ímpares é {si}")
