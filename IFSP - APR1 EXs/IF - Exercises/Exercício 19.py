x=float(input("Qual foi o valor gasto com a compra sem desconto:"))

val1=x*0.95
val2=x*0.90
val3=x*0.80

if x<=100:
    print(f"O desconto da compra foi de 5%, totalizando um gasto de {val1}")
elif 100<x<200:
    print(f"O desconto da compra foi de 10%, totalizando um gasto de {val2}")
else:
    print(f"O desconto da compra foi de 20%, totalizando um gasto de {val3}")
