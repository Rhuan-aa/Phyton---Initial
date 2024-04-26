n=float(input("Digite uma nota positiva(negativa, para finalizar): "))
nmai6=0
nmen6_maii4=0
nmen4=0
while n>=0:
    if n>=6:
        nmai6=nmai6+1
    elif 6>n>=4:
        nmen6_maii4=nmen6_maii4+1
    else:
        nmen4=nmen4+1
    n=float(input("Digite uma nota positiva(negativa, para finalizar): "))
print(f"Quantidade de notas maiores ou iguais a 6: {nmai6}")
print(f"Quantidade de notas menores que 6 e maiores ou iguais a 4: {nmen6_maii4}")
print(f"Quantidade de notas menores que 4: {nmen4}")

