t=0
n=1
melhor_t=float('inf')
melhor_n=0
ttotal=0
while n<=10:
    t=int(input(f"Digite o tempo da {n} volta: "))
    ttotal=ttotal+t
    if t<melhor_t:
        melhor_t=t
        melhor_n=n
    n+=1
print(f"A melhor volta foi {melhor_n} e seu tempo foi {melhor_t}")
print(f"A média de tempo das 10 voltas foi {ttotal/10}")
    
