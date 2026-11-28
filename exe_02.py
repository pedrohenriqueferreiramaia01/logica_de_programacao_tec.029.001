# todo: crie um programa que receba do usuario o nome, massa e a altura
# e calcule seu imc (indice de massa corporal),
# apos mostra ,o IMC, o programa deve informa de acordo com o 
# valor do seu IMC:
# IMC < 18.5:"usuàrio està abaixo do peso"
# IMC < 25: "usuàrio està no peso ideal"
# IMC < 30: " usuário está acima do peso"
# IMC < 35: "usuario està obeso"
# IMC < 40: "usuario esta com obesidade nivel 2"
# se não estiver em nenhum dos casos acima:
# "usuario esta com obesidade morbina"
# note: imc = massa/(altura**2)

# entrada de dados 
nome = input("informe seu nome: ").strip().title()
massa = float(input("informe sua massa muscular: ").replace(",","."))
altura = float(input("informe sua altura: ").replace(",","."))

if massa/(altura**2):
     print(f"seu{nome},seu IMC e:{massa/altura**2}")
elif "espera-se IMC < 18.5":  
     print("usuario esta abaixo do peso")

if massa/(altura**2):
    print(f"seu {nome}, seu IMC e{massa/altura**2}")
elif "espera-se IMC < 25":
  print("usuario esta no peso ideal")

if massa/(altura**2):
    print(f"seu{nome}, seu IMC e {massa/altura**2}")
elif  "espera-se IMC < 30":
    print("usuario esta acima do peso")

if massa/(altura**2):
        print(f"seu{nome},seu IMC{massa/altura**2}")
elif "espera-se IMC < 35":
      print("usuario esta obeso")

if massa/(altura**2):
    print(f"seu{nome},seu IMC e{massa/altura**2}")
elif "espera-se IMC < 40":
    print("usuario esta com obesidade nivel 2")



