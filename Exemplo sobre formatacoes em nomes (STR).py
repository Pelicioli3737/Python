nome = str(input("Digite seu nome: "))

nome = nome.strip()  # Remove espaços em branco no início e no final do nome

nome = nome.capitalize()  # Coloca a primeira letra do nome em maiúscula
             
nome = nome.title()  # Coloca a primeira letra de cada palavra em maiúscula

print(f"Olá, {nome}!")

#Mas tambem da pra encadeiar tudo, ou seja fazer tudo numa linha so, pra economizar linhas de codigo

""
nome = nome.strip().capitalize() ou nome = nome.strip().title()

print(f"Olá, {nome}!")

ou ate mesmo desse jeito, que é o mais economico de todos

nome = str(input("Digite seu nome: ")).strip().title()

print(f"Olá, {nome}!")



se voce quiser separar o nome do sobrenome, voce pode fazer assim:

primeiro, ultimo = nome.split(" ") #isso vai separar o nome em duas variaveis, a primeira palavra vai pra primeiro e a segunda vai pra ultimo
                                    as aspas servem pra dizer que o separador é o espaco, se fosse uma virgula, seria assim: nome.split(",")

print(f"Olá, {primeiro} {ultimo}!")

print(f"Olá, {primeiro}!") #isso vai imprimir apenas o primeiro nome
""