N=int(input("Digite um valor: "))
numeros=[]
contagem=[0]*10001

for i in range(N):
    X=int(input("Digite um numero: "))
    numeros.append(X)

for num in numeros:
    contagem[num]+=1

frequencia_max=float('-inf')
for freq in contagem:
    if freq>frequencia_max:
        frequencia_max=freq

n_mais_freq=[]
for i in range(len(contagem)):
    if contagem[i]==frequencia_max:
        n_mais_freq.append(i)

if len(n_mais_freq) == 1:
    print(f"O número que aparece mais vezes é: {n_mais_freq[0]}")
else:
    print("Há um empate entre os seguintes números:")
    for num in n_mais_freq:
        print(num)
