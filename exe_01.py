1# todo:crie um programa que recebe do usuario o valor da gasolina
2#è do etanol, e informe para o usuario qual o melhor combustivel
3#para se abastecer
4#note: compensa mais abastecer com etanol caso o valor do etanol
5# corresponda a atè 75% do valor da gasolina.
6#note: e não se esqueçam do detalhe mais importante de todos:

#entrada de dados 
gasolina = float(input("informe um valo: ").replace(",","."))
etanol = float(input("informe um valor: ").replace(",","."))

if etanol <= gasolina * 0.75:
    print(" melhor abastecer com etanol.")
else:
    print("melhor abastecer com gasolina.")


