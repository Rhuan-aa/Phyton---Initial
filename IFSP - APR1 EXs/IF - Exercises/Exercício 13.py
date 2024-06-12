x=int(input("Quantos livros deseja comprar?"))
crita=x*0.25+7.50
critb=x*0.50+2.50

if crita<critb:
        print(f"O valor pelo critério A é {crita}, já pelo critério B é {critb}, dessa forma o critério A é mais vantajoso.")
elif crita>critb:
        print(f"O valor pelo critério A é {crita}, já pelo critério B é {critb}, dessa forma o critério B é mais vantajoso.")
else:
        print(f"O valor pelo critério A é {crita}, já pelo critério B é {critb}, contudo não há um critério mais vantajoso.")
