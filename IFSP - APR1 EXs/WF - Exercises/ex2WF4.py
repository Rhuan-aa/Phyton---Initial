n=int(input("Digite um inteiro longo: "))
soma=0
while n>0:
    digito=n%10
    print(digito)
    if digito%2==0:
        soma+=digito
    n//=10
print(soma)
