n=int(input("Digite um numero inteiro: "))
quant_digit=0
numerop=(f"{n}")
numeron=(f"{n}")

if n>=0:
    for i in numerop:
        quant_digit+=1
    print(quant_digit)
else:
    quant_digit-=1
    for i in numeron:
        quant_digit+=1
    print(quant_digit)
