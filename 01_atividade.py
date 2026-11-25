nome = input("informe seu nome: ")
email = input("informe seu email: ")
cpf = input("informe seu cpf: ")
telefone = input("informe seu numero: ")
idade = input("informe sua idade: ")
altura = input("informe sua altura: ")

#conversao de tipo
idade = int(idade)
altura = float(altura)

#saida de dados 
print(f"nome: {nome}, Tipo {type(nome)}")
print(f"email: {email}, Tipo {type(email)}")
print(f"cpf: {cpf}, Tipo {type(cpf)}")
print(f"telefone: {telefone}, Tipo {type(telefone)}")
print(f"idade: {idade}, Tipo {type(idade)} ")
print(f"altura: {idade}, Tipo {type(altura)}")
