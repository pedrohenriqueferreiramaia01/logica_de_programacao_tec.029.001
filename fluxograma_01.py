nome = input("informe seu nome: ").strip().title()
email = input("informe seu email: ").strip().lower()
cpf = input("informe seu cpf: ").strip()
telefone = input("informe seu numero: ").strip()
idade = input("informe sua idade: ")
altura = input("informe sua altura: ")

#conversao de tipo
idade = int(idade)
altura = float(altura).replece(",",".")

#saida de dados 
print(f"nome: {nome}, Tipo {type(nome)}")
print(f"email: {email}, Tipo {type(email)}")
print(f"cpf: {cpf}, Tipo {type(cpf)}")
print(f"telefone: {telefone}, Tipo {type(telefone)}")
print(f"idade: {idade}, Tipo {type(idade)} ")
print(f"altura: {idade}, Tipo {type(altura)}")
