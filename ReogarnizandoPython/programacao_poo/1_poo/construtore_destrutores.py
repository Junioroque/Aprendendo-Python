#metodo construtor e destrutor: __init__ e __del__

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print(f'{self.nome} está latindo: Au Au!')

    def __del__(self):
        print(f'O cachorro {self.nome} foi deletado da memória.')
        
dog = Cachorro('Rex', 'Marrom')
dog.latir()
print('Continuano.......')

print('Ola mundo!')
print('Ola mundo!')
del dog
print('Ola mundo!')