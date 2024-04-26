A=[]
B=[]
C=[]
for i in range(5):
    n=int(input("Digite um valor para a lista A: "))
    A.append(n)
for i in range(5):
    n=int(input("Digite um valor para a lista B: "))
    B.append(n)
for i in range(10):
    n=int(input("Digite um valor para a lista C: "))
    C.append(n)
A+=C[:4]
B+=C[5:]
print(A)
print(B)
