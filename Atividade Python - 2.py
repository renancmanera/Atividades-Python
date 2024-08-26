#Atividade Python - 2

#1)

def contador(horas):
    segundos = horas * 3600
    minutos = 0
    while segundos >= 60:
        segundos -= 60
        minutos += 1
    return f'{minutos} minutos e {segundos} segundos'

print(contador(42))

#2)

def montante(capital_inicial, juros_por_ano, periodo_em_ano):
    montante = capital_inicial * (1 + juros_por_ano) * periodo_em_ano
    return montante
print(montante(100,12,1))

#3)

def cambio(real):
    dolar = real / 5.1
    return round(dolar,2)

print(cambio(1200))

#4)

def primos(x, y):
    primos = []
    for numero in range(x, y + 1):
        if numero > 1: 
            for i in range(2, numero):
                if (numero % i) == 0: 
                    break
            else:
                primos.append(numero) 
    return primos

print(primos(2, 100))



