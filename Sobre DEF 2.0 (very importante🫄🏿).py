def main():
    x = int(input("Digite um numero: "))
    print(f"{x}","ao quadrado é", square(x)) #aqui daria errado, pois square nao esta definido, por isso que def square abaixo:

def square(x):
    x * x #return é pra o valor voltar, inves de ficar na def, com isso o resultado de x * x vai voltar pro square ali em cima

main()