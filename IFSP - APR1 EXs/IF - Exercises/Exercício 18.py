i=int(input("Informe sua idade:"))

if i==16 or i==17:
        print("Se trata de um eleitor facultativo")
elif 65>=i>=18 :
        print("Se trata de um eleitor obrigatório")
elif 65<i:
        print("Se trata de um eleitor dispensado")
else:
        print("Se trata de um não-eleitor")
