n=int(input("Digite um numero natural: "))
a=0
b=1
print("0")
print("1")    

for i in range(1,n):
    c=a+b
    a=b
    b=c
    i+=1
    print(c)

