x=int(input("Digite um numero inteiro:"))
y=int(input("Digite outro numero inteiro:"))
z=int(input("Digite mais um numero inteiro:"))

if x>=y>=z:
        print(f"A é igual a {z},já o B é {y} e por ultimo o C é igual a {x}")
elif x>=z>=y:
        print(f"A é igual a {y},já o B é {z} e por ultimo o C é igual a {x}")
elif y>=z>=x:
        print(f"A é igual a {x},já o B é {z} e por ultimo o C é igual a {y}")
elif y>=x>=z:
        print(f"A é igual a {z},já o B é {x} e por ultimo o C é igual a {y}")
elif z>=x>=y:
        print(f"A é igual a {y},já o B é {x} e por ultimo o C é igual a {z}")
else:
        print(f"A é igual a {x},já o B é {y} e por ultimo o C é igual a {z}")
