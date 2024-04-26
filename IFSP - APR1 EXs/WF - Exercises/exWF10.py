nota=int(input("Digite uma Nota Positiva (Negativa para finalizar): "))
num_alu=0
maior_nota = float('-inf')
menor_nota = float('inf')
while nota>=0:
    num_alu=num_alu+1
    nota=int(input("Digite uma Nota Positiva (Negativa para finalizar): "))
    if nota<0:
        break
    if nota>maior_nota:
        maior_nota=nota
    if nota<menor_nota:
        menor_nota=nota
    
print(f"Numero de Alunos: {num_alu}")
print(f"Maior Nota: {maior_nota}")
print(f"Menor Nota: {menor_nota}")
