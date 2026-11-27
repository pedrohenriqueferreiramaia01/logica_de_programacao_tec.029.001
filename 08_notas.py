#entrada de dados 
nome = input("informe seu nome: ").strip().title()
nota1 = int(input("informe a primeira nota:"))
nota2 = int(input("informe a segunda nota: "))

#processamento de dados 
media = (nota1+nota2)/2

#exibe a nota
print(f"Media: (media)")

#estrutura de decisao
if media >=7:
 print(f"(nome) està aprovado.")
elif media>=5:
 print(f"(nome) està de recuperação.")
else:
 print(f"(nome) està reprovado.")