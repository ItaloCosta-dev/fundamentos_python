resultado = None #indica que a variável ainda não tem valor
print(resultado)

nome, _, idade = ("Italo", "Masculino", 30) # ignora o segundo valor
print(nome, _, idade)

x = 10
def alterar():
    global x
    x = 20 # modifica a variável global
alterar()
print(x) # 20