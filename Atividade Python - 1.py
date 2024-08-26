#Atividade Python - 1

#1)

def funcao(nome):
    return(f'Saudações {nome}')
print(funcao('Renan'))

#2)

def operacoes(x,y):
    return(x+y, x-y,x*y, x/y)
print(operacoes(1,2))

#3)

def faixa_etaria(idade):
    if 0 < idade <= 12:
        return('Criança')
    elif 13 < idade <= 17:
        return('Adolescente')
    elif 18 < idade <= 64:
        return('Adulto')
    elif 65 < idade:
        return('Idoso')
    else:
        return('Inválido')
print(faixa_etaria(20))

#4)

#F = C x 1,8 + 32

def formula(celsius):
    farenheit = celsius * 1.8 + 32
    return(farenheit)
print(formula(30))

#5)

#A regra básica é que um ano é bissexto se for divisível por 4. 
#No entanto, existem algumas exceções a essa regra. 
#Anos que são divisíveis por 100 não são bissextos, a menos que também sejam divisíveis por 400.

def ano_bissexto(ano):
    if ano % 4 == 0:
            if ano % 100 == 0:
                  if ano % 400 == 0:
                    return True
                  else:
                       return False
            else:
                 return True
    else:
         return False
print(ano_bissexto(2004))

#6)

def calculadora_imc(altura,peso):
    imc = peso / altura**2
    if imc < 18.5:
        return(f'Baixo peso. IMC = {imc:.2f}')
    elif 18.5 < imc < 24.99:
        return(f'Normal. IMC = {imc:.2f}')
    elif 25 < imc < 29.99:
        return(f'Sobrepeso. IMC = {imc:.2f}')
    elif 30 <= imc:
        return(f'Obesidade. IMC = {imc:.2f}')
print(calculadora_imc(1.82,79))

#7)

import random
import string
def gerarSenha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha
print(gerarSenha(10))

#8)

import string
def verif_palind(palavra):
    palavra = palavra.replace(' ', '').lower()
    return palavra == palavra[::-1]
print(verif_palind('a mae te ama'))

#9)

import random

def acerteNumero():
    computador = random.randint(1,101)
    tentativa = None
    tentativas = 0

    while tentativa != computador:
       tentativa = int(input('Chute um número entre 1 e 100: ')) 
       tentativas += 1
       if tentativa < computador:
            print("Maior!")
       elif tentativa > computador:
            print("Menor!")
    
    print(f"Depois de {tentativas} tentativas você acertou o número {computador} que eu pensei!")

acerteNumero()

#10)

def triangulo(a,b,c):
    if a == b == c:
        return('Triângulo equilátero')
    elif a == b != c or a == c != b or b == c != a:
        return('Triângulo isóceles')
    elif a != b != c:
        return('Triângulo escaleno')
print(triangulo(1,1,2))
