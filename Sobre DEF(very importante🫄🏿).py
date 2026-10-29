

#def hello(x = "World"):            isso fala que se o programa nao receber nada externo ele vai ser = "World"
'''
def hello(x):                         #o "x" ali fala que a DEF pode receber alguma entrada externa digamos, nesse exemplo "name", a variavel
    print("Hello, ", x)               # se nao tivesse nada ali nos () ele nao poderia receber nada externo e daria erro  
name = input("What is your name? ")
hello(name)
'''








#aqui comeca a desgracada, ou a coisa mais foda que ja vi 

def main():
    name = input("What is your name? ")
    hello(name)         #aqui hello nao esta definido e vai dar errado por isso que def hello abaixo:

def hello(x):
    print("Hello,", x) #aqui sim vai dar bom, pois o main chama o hello e ele esta definido, e o (x) permite que name seja implementado
                       #se eu tentasse inves de "Hello, x" e colocasse "Hello, name", daria erro pois name so esta definido dentro do main, entao fora ele nao vale nada(Puta merda, isso foi do cacete!(Billy Bruto))

main()
