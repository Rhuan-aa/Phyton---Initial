t=input("Digite um telefone: ")
tradução=""
numeros="0123456789"
t2="ABC"
t3="DEF"
t4="GHI"
t5="JKL"
t6="MNO"
t7="PQRS"
t8="TUV"
t9="WXY"
hifen="-"

for i in range(len(t)):
    if t[i] in numeros:
        tradução+=t[i]
    if t[i] in t2:
        tradução+="2"
    if t[i] in t3:
        tradução+="3"
    if t[i] in t4:
        tradução+="4"
    if t[i] in t5:
        tradução+="5"
    if t[i] in t6:
        tradução+="6"
    if t[i] in t7:
        tradução+="7"
    if t[i] in t8:
        tradução+="8"
    if t[i] in t9:
        tradução+="9"
    if t[i] in hifen:
        tradução+="-"
print(tradução)
