cod=int(input("Digite o código do curso: "))
tcadi=0
while cod > 0:
    vag=int(input("Digite o numero de vagas do curso: "))
    masc=int(input("Digite o numero de candidatos do sexo masc.: "))
    fem=int(input("Digite o numero de candidatos do sexo fem.: "))
    cadivag=(masc+fem)//vag
    cadi=masc+fem
    porcfem=(100*fem)/(masc+fem)
    maior_candivag=0
    codmaior_candivag=float('-inf')
    if cadivag>maior_candivag:
        maior_candivag = cadivag
        codmaior_candivag=cod
    tcadi=tcadi+cadi
    print(f"No curso {cod}, o numero de candidato/vaga é {cadivag} e porcentual feminino do curso é {porcfem}%")
    cod=int(input("Digite o código do curso: "))
print(f"A maior relação candidato/vaga acontece no curso {codmaior_candivag} e seu valor é de {maior_candivag}")
print(f"O total de candidatos é {tcadi}")
