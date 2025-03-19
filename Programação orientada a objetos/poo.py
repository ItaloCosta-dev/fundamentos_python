#1 - Classes e objetos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#Criando um objeto
pessoa = Pessoa("Italo", 30)
print(pessoa.nome)

#2 - Atributos e métodos
class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Carro:{self.modelo}, Ano:{self.ano}"

carro1 = Carro("Civic", 2020) 
print(carro1.detalhes())  

#3 - Herança
class Animal:
    def som(self):
        print("Som do animal")

class Cachorro(Animal):
    def som(self):
        print("Au au!")

dog = Cachorro()
dog.som()

#4 - Polimorfismo
class Gato:
    def som(self):
        print('Miua!')

class Cachorro:
    def som(self):
        print("Au au!")

def emitir_som(animal):
    animal.som()

emitir_som(Gato())
emitir_som(Cachorro())

#5 - Encapsulamento
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
    
    def mostrar_saldo(self):
        return self.__saldo

conta = ContaBancaria(1000)
print(conta.mostrar_saldo())

#6 - Métodos especiais
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} custa R${self.preco}"

produto1 = Produto("Notebook", 3500)
print(produto1)

#7 - Manipulação de arquivos
with open("dados.txt", "w") as arquivo:
    arquivo.write("Python é incrível!")

with open("dados.txt", "r") as arquivo:
    print(arquivo.read())

#8 - Tratamento de erros 
try: 
    x = int(input("Digite um número:"))
    resultado = 10 / x
except ValueError:
    print("Você precisa digitar um número.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
else:
    print("Resultado", resultado)
finally: 
    print("Fim do programa.")
