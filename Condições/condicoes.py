#Estrutura básica do IF
idade = 18
if idade >= 18:
    print("Você é maior de idade")

#Usando o else
idade = 16
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

#Usando o elif
nota = 79
if nota >= 90:
    print("Nota A")
elif nota >= 80:
    print("Nota B")
elif nota >= 70:
    print("Nota C")
else: print("Reprovado") 

#Condição com operadores
#Exemplo com and
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")

#Exemplo com or
tem_passaporte = False
tem_visto =True

if tem_passaporte or tem_visto:
    print("Pode viajar")

#Exemplo com not
chovendo = False
if not chovendo:
    print("Vamos sair!")

#If em uma linha - ternário
idade = 18
mensagem = "maior de idade" if idade >=18 else "menor de idade"

#Verificando múltiplos valores com in
fruta = "banana"

if fruta in ["banana", "maça", "uva"]:
    print("Fruta disponível")

#Aninhamento dentro do if
idade = 20
tem_carteira = True

if idade >= 18:
    if tem_carteira:
        print("pode dirigir")
    else:
        print("Não pode dirigir, precisa de carteira")
else:
    print("Não pode dirigir, precisa ser maior de idade")

#Comparações avançadas
#Forma tradicional
idade = 25
if idade >=18 and idade <=60:
    print("Adulto")

#forma simplificada
idade = 25
if 18 <= idade <=60:
    print("adulto")

#lidando com valores vazios
nome = ""

if nome:
    print("Nome preenchido")
else: 
    print("nome não informado")

#usando o match case (Python 3.10+)
opcao = 2

match opcao:
    case 1:
        print("Opção 1 escolhida")
    case 2:
        print("Opção 2 escolhida")
    case _:
        print("Opção inválida")    
