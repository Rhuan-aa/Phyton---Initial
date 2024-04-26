n=int(input("Digite um inteiro longo: "))
soma=0
i=1
while n>0:
    digito=n%10
    if i%2!=0:
        soma+=digito
    n//=10
    i+=1
    print(soma)
print(soma)
