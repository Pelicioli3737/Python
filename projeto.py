turma = [ {"nome": "ana", "nota": [8.0, 7.5, 9.0]},
          {"nome": "bruno", "nota": [6.0, 7.0, 8.5]},
          {"nome": "carla", "nota": [9.5, 8.0, 7.5]},
          {"nome": "daniel", "nota": [7.0, 6.5, 8.0]}
]
if __name__ == "__main__":
    for aluno in turma:
        media = sum(aluno["nota"]) / len(aluno["nota"])
        print(f"A média de {aluno['nome']} é {media:.2f}")