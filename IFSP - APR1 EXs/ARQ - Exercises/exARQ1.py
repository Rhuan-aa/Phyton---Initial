# Dicionários
dic={'SC123456':('Aluno 1','aluno1@ifsp.edu.br'),
     'SC456789':('Aluno 2','aluno2@ifsp.edu.br'),
     'SC901234':('Aluno 3','aluno3@ifsp.edu.br')}

## O Arquivo Existe?
def existe_arq(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

## Função
def count_lines(file):
    ref_arq=open(file, 'r')
    lines=ref_arq.readlines()
    num_lines=len(lines)
    return num_lines
    
# Gravando arquivo
if len(dic):
    ref_arq=open('cadastro_alunos.txt','w')
    for aluno in dic:
        RA=aluno
        nome, email = dic[aluno]
        linha = RA+ "\t" + nome+ "\t" + email + "\n"
        ref_arq.write(linha)
    ref_arq.close()
    print("Arquivo gravado com sucesso")
print(count_lines('cadastro_alunos.txt'))
