#Atividade Python - 3

#1)

soma = lambda a, b, c: a + b + c if a > 0 and b > 0 and c > 0 else 'Erro'

print(soma(1,2,3))
print(soma(-1,2,3))

#2)

multiplicacao = lambda a, b, c: a * b * c if a != 0 and b != 0 and c != 0 else 'Erro'

print(multiplicacao(2,3,4))
print(multiplicacao(2,0,4))

#3)

concatenacao = lambda nome1, nome2: nome1 + nome2 if len(nome1) > 3 and len(nome2) > 3 else 'Erro'

print(concatenacao('Olá', 'Mundo'))

#4)

media = lambda lista: sum(num for num in lista if num >= 0) / len([num for num in lista if num >= 0])
print(media([1, -2, 3, -4, 5]))

#5)

numeros = [3, 4, 5, 6, 7, 8, 9, 10, 11]
primos = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)), numeros))
print(primos) 

#6)

teste = lambda x: (x ** 2) - 1 if x % 2 == 0 else 'Erro'
print(teste(4))
print(teste(3))

#7)

ordenar = lambda pessoas: sorted(pessoas, key=lambda pessoa: pessoa['idade'], reverse=True)
print(ordenar([{'nome': 'Ana', 'idade': 25}, {'nome': 'João', 'idade': 22}, {'nome': 'Carlos', 'idade': 30}]))

#8)

farenheit_para_celcius = lambda f: ((f - 32) * 5/9)
print(farenheit_para_celcius(32))
print(round(farenheit_para_celcius(250), 1))

#9)

celcius = [0,20,100]
celcius_para_farenheit = list(map(lambda celsius: celsius * 9/5 + 32, celcius))
print(celcius_para_farenheit)

#10)

from functools import reduce

numeros = [1, 2, 3, 4]
multiplicacao = reduce(lambda x, y: x * y, numeros) if reduce(lambda x, y: x * y, numeros) <= 50 else 'Erro'
print(multiplicacao)

#11)

numeros = [1, 3, 5, 15, 30, 35]
multiplos_3_5 = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, numeros))
print(multiplos_3_5)

#12)

ordem_inversa = lambda lista: lista[::-1] if len(lista) % 2 == 1 else lista
print(ordem_inversa('Python'))
print(ordem_inversa('Lambdas'))

#13)

lista = [1, 2, 3, 4]
elevar_ao_cubo = list(map(lambda num: num**3 if num <= 2 else num, lista))
print(elevar_ao_cubo)

#14)

lista = [-5, -1, 0, 3, 7]
transformar = list(map(lambda x: abs(x) if x < 0 else x, lista))
print(transformar)

#15)

receber_lista_strings = lambda lista: [len(string) for string in lista]
print(receber_lista_strings(['teste', 'oi', 'renan']))

#16)

ordenar = lambda pessoas: sorted(pessoas, key=lambda pessoa: len(pessoa[0]), reverse=True)
print(ordenar([('Ana', 25), ('João', 22), ('Carlos', 30)]))

#17)

primo = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1) if i % 2 != 0 and i % 3 != 0)
print(primo(25)) 

#18)

maiuscula = lambda x: [x.upper() for x in x]
print(maiuscula(["Python", "Lambda", "Functions"]))

#19)

lista = ["Ana", "João", "Carlos", "Amanda"]

nomes_A = list(filter(lambda nome: nome.startswith("A") and len(nome) <= 5, lista))
print(nomes_A)

#20)

pessoas = [('Amanda', 20), ('Angelo', 25), ('Renan', 17), ('Rodrigo', 30)]

nomes = list(filter(lambda x: x[1] > 18 and not x[0].startswith('A'), pessoas))
print(nomes)







