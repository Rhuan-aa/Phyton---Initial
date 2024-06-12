def exibir_algarismos(numero):
    # Caso base: se o número for menor que 10, é um dígito único
    if numero < 10:
        print(numero)
    # Caso recursivo: dividir o número por 10 para obter o próximo dígito
    else:
        exibir_algarismos(numero // 10)
        print(numero % 10)

x=int(input("Digite um numero: "))
print(exibir_algarismos(x))
        
