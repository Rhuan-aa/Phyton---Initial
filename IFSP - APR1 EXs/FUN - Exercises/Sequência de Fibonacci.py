def sequencia_fibonacci(a, b, n):
    if a < n:
        print(a," ",end="")
    if b < n:
        sequencia_fibonacci(b, a + b, n)
nro=int(input('Digite o valor de parada da sequência de Fibonacci: '))
sequencia_fibonacci(0,1,nro)
