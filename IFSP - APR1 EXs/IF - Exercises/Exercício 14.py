a=int(input("Qual o valor de A?"))
b=int(input("Qual o valor de B?"))
c=int(input("Qual o valor de C?"))

delt=b**2-4*a*c
x1=(-b+delt**(1/2))/2*a
x2=(-b-delt**(1/2))/2*a

if delt>0:
    print(f"As raízes da equação são iguais a {x1} e {x2}")
elif delt==0:
    print(f"A raíz da equação é igual a {x1}")
else:
    print(f"Não existem raízes reais para essa equação")
