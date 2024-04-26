n=int(input("Digite um numero inteiro maior que zero: "))
i=int(input("Digite outro numero inteiro maior que zero: "))
j=int(input("Digite mais um numero inteiro maior que zero: "))
r=0
while r<=n-1:
    if r%i==0 and not r%j==0 or r==0:
        print(r)
        r+=1
    elif r%j==0 and not r%i==0:
        print(r)
        r+=1
    elif r%j==0 and r%i==0:
        print(r)
        r+=1
    else:
        n+=1
        r+=1
