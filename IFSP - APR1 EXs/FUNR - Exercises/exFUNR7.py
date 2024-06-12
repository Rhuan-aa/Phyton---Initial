def vert_num(num):
    if num==0:
        return ""
    else:
        print(num%10)
        vert_num(num//10)


x=int(input("Digite um numero: "))
print(vert_num(x))
        
