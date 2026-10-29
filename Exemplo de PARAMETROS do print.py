nome = str(input("Digite seu nome: "))

print("Seu nome é", end=" ", sep="") #exemplo de mudar a formatacao do print, o normal seria end="n\", que o n\ faz ir pra proxima linha, mas sem nada ele fica na mesma
                                     # o sep="" fala oq teria antes da virgula, o normal é sep= " ", que coloca um espaco automaticamente
print(nome)

print("hello,", nome, sep="")
