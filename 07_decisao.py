#entrada de dados
massa = float(input("informe a massa muscular: ").replace(",","."))
altura = float(input("informea altura: ").replace(",","."))

if massa <=140 and altura >=1.15:
    print(f"Entrada do usuàrio permitido.")
else:
    print(f"Entrada do usuàrio negada.")