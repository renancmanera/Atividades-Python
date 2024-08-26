#Atividade Python - 5

#1)

tupla = (1, 2, 2, 3, 4, 4, 5)
tupla_sem_duplicatas = tuple(set(tupla))
print(tupla_sem_duplicatas)

#2)

tupla01 = (1, 2, 3)
tupla02 = (3, 4, 5)
tupla03 = set(tupla01 + tupla02)
print(tupla03)

#3)

tupla = (23, 1, 56, 3, 78, 2)

def tupla_escolhida(tupla):
    return min(tupla), max(tupla)

print(tupla_escolhida(tupla))

#4)

tupla = (("Alice", 25), ("Bob", 22), ("Charlie", 23))
tupla_ordenada = sorted(tupla, key=lambda x: x[1])

print(tupla_ordenada)

#5)

tupla = (1, "a", 2.5, "b", 3)

qtd_int = 0
qtd_str = 0
qtd_float = 0

for elemento in tupla:
    if type(elemento) == int:
        qtd_int += 1
    elif type(elemento) == str:
        qtd_str += 1
    elif type(elemento) == float:
        qtd_float += 1

print(f"Quantidade de inteiros: {qtd_int}")
print(f"Quantidade de strings: {qtd_str}")
print(f"Quantidade de floats: {qtd_float}")

#6)

tupla1 = (1, 2, 3, 4)
tupla2 = (3, 4, 5, 6)

elementos_comuns = tuple(set(tupla1) & set(tupla2))

print(elementos_comuns)

#7)

lista_de_tuplas = [("a", 1), ("b", 2), ("c", 3)]
dicionario = dict(lista_de_tuplas)
print(dicionario) 

#8)

tupla = (1, 2, 3, 4, 5, 6)

def tupla_pares(tupla):
    tupla_nova = tuple(i for i in tupla if i % 2 == 0)
    return tupla_nova

print(tupla_pares(tupla))

#9)

tupla = ((1, 2), (3, 4), (5, 6))
print(tupla[2][1])

#10)

tupla = (10,5)

def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b  

def divisao(a,b):
    return a/b

funcoes_totais = [soma, subtracao, multiplicacao, divisao]

for funcao in funcoes_totais:
    print(funcao(tupla[0],tupla[1]))


