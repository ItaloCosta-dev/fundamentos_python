#Sintaxe básica
print("Olá, mundo!")

#Tipos de dados
a = 10   # int
b = 3.14 # float

#Strings
nome = "Alice"
mensagem = 'Bem-vindo ao Python!'

#Listas
lista = [1, 2, 3, 4]
lista.append(5)  # Adiciona 5 à lista

#Tuplas
tupla = (1, 2, 3)

#Dicionários
dicionario = {"chave1": "valor1", "chave2": "valor2"}

#Conjuntos
conjunto = {1, 2, 3}

#Condicionais: if, elif, else
idade = 18
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

#Laços: for e while
# Laço for
for i in range(5):  # Vai de 0 a 4
    print(i)

# Laço while
x = 0
while x < 5:
    print(x)
    x += 1

#Funções
def saudacao(nome):
    return f"Olá, {nome}!"
print(saudacao("João"))

#Funções com parâmetros
def saudacao(nome="Visitante"):
    return f"Olá, {nome}!"

#Manipulações de strings
texto = "Python"
print(texto[0])  # P
print(texto[1:4])  # yth
print(len(texto))  # 6

#Métodos de strings
frase = "olá mundo"
print(frase.upper())  # "OLÁ MUNDO"
print(frase.replace("mundo", "Python"))  # "olá Python"

#Métodos de listas
lista = [1, 2, 3]
lista.append(4)  # Adiciona 4
lista.pop()  # Remove o último item

#Métodos de dicionários
dicionario = {"nome": "João", "idade": 25}
print(dicionario["nome"])  # "João"

#Abrindo e lendo aqruivos
with open('exemplo.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)

#Escrevendo em arquivos
with open('exemplo.txt', 'w') as file:
    file.write("Este é um texto de exemplo")

#Exceções e tratamentos de erros
#Try, excepct:
try:
    a = 10 / 0
except ZeroDivisionError:
    print("Não é possível dividir por zero")

#importando módulos
import math
print(math.sqrt(16))  # 4.0

#Classes e objetos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos"

pessoa1 = Pessoa("Maria", 30)
print(pessoa1.saudacao())

#Herança
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def saudacao(self):
        return f"Sou estudante de {self.curso}, meu nome é {self.nome} e tenho {self.idade} anos"

estudante1 = Estudante("Carlos", 22, "Engenharia")
print(estudante1.saudacao())

#List Comprehension
quadrados = [x**2 for x in range(10)]
print(quadrados)

#Decoradores
def meu_decorador(func):
    def wrapper():
        print("Antes da função")
        func()
        print("Depois da função")
    return wrapper

@meu_decorador
def ola():
    print("Olá, Mundo!")

ola()

#Geradores
def contador():
    i = 1
    while True:
        yield i
        i += 1

gen = contador()
print(next(gen))  # 1
print(next(gen))  # 2

#Bibliotecas populares
import numpy as np
arr = np.array([1, 2, 3])
print(arr + 2)  # [3 4 5]

import pandas as pd
df = pd.DataFrame({'Nome': ['Alice', 'Bob'], 'Idade': [23, 25]})
print(df)

import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()



