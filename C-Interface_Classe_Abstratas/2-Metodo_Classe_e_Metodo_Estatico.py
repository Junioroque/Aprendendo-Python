class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        
   # def criar_de_data_nascimento(self, ano, mes, dia , nome):
   #     idade = 2022 - ano
   #     return Pessoa(nome, idade)
    #outra forma de resolver a instacia usando um decorador calssmethod
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia , nome):
        idade = 2022 - ano
        return cls(nome, idade)
    
    #declara função estatica
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
p = Pessoa("Jorge", 33)

print(p.nome, p.idade)
print("======================")
#criei 2 instancia
p2 = Pessoa().criar_de_data_nascimento(1994, 3, 21, "João")
#print(p2.nome, p2.idade)
print("======================")
#Usando o classmethod
p3 = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Jorge")
print(p3.nome, p3.idade)
print("'=====================")
#Usando metodo estatico
print(Pessoa.e_maior_idade(33))
print(Pessoa.e_maior_idade(4))