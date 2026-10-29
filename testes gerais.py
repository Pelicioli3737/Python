nota = float(input("Digite a nota do aluno: "))
print("A nota do aluno é:",nota) 
#Um jeito de por variável dentro de um texto (str)
#print(f"A nota do aluno é: {nota}")
#Outro jeito de por variável dentro de um texto (str)

if 0 > nota or nota > 10:
    print("O incopetente digite um nota que vale (Dica radical: ter que ser entre 0 e 10)")
elif nota >= 8.75:
    print("Aluno aprovado, parabéns tu é cuiudo")
elif nota >= 8:
    print("Aluno aprovado, foi bem")
elif nota >= 6:
    print("Aluno aprovado! Passou na arroz e feijão")
elif nota >= 5:
    print("Bateu na trave, mas vai ter que fazer o ano todo de novo kkkkkkkkkkkkkkkkkkkkkk")
elif 2 <= nota < 5:
    print("heeeeeee, sem comentarios, reprovado")
else:
    print("Ai é foda, nem tento, REPROVADO")





