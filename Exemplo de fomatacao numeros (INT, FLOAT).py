x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))
z = x + y


print(round(x + y, 0)) #isso vai arredondar o resultado de x + y para 0 casas decimais

print(f"O resultado de {x} + {y} é {round(x + y, 2)}") #isso vai arredondar o resultado de x + y para 2 casas decimais e printar o resultado com uma frase

print(f"{z: ,}") #isso vai coloca ( , ) a cada 3 digitos, muito bom com numeros grandes, exp 1,000,000.0, e sim os gringo usa virgula (bando de loco)

