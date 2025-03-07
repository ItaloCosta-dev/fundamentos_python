x = 10 # variável global

def  minha_funcao():
    y = 5 # variável local
    print (x + y) # Acessa as variáveis global e local)

minha_funcao()
print(y) # 'x' não uma variável local