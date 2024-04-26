n=int(input("Digite um inteiro longo: "))
quant_pares=0
quant_impares=0
while n>0:
    digito=n%10
    if digito%2==0:
        quant_pares+=1
    if digito%2!=0:
        quant_impares+=1
    n//=10
print(f"A quantidade de digitos pares é {quant_pares}, e de digitos impares é {quant_impares}")
