exp=1
d=50
soma=0
while exp<=50 and d>=1:
    print(2**exp/d)
    soma+=2**exp/d
    exp+=1
    d-=1
print(f"A soma é {soma}")
    
