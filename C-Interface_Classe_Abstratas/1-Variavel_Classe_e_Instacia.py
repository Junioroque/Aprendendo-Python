class Estudante:
    escola = "Melhor Plataform de Estudo - Dio"
    print("Link da DIO")
    
    #instancia
    def __init__(self, nome , matricula):
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_Valores(*objs):
    for obj in objs:
        print(obj)
        
aluno_1 = Estudante("Carla", 1)
aluno_2 = Estudante("Bruna", 2)

print(aluno_1)
print(aluno_2)

aluno_1.matricula = 3

print(aluno_1)
print(aluno_2)

aluno_2.escola = "Dio - Avançado"

mostrar_Valores(aluno_1, aluno_2)