def ret_carac(f):
    if f=="":
        return 0
    return 1+ret_carac(f[1:])

fra=input("Digite uma string")
print(f"A string possui {ret_carac(fra)} caracteres.")
