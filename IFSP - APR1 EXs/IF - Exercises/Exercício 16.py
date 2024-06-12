x=float(input("Digite um numero:"))
y=float(input("Digite outro numero:"))
z=float(input("Digite mais um numero:"))

if x>y>z or x>z>y:
        print(f"{x} é o maior dentre os três números")
elif y>x>z or y>z>x:
        print(f"{y} é o maior dentre os três números")
else:
        print(f"{z} é o maior dentre os três números")
