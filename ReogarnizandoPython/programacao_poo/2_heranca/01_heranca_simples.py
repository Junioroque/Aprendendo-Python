class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas    
        
    def ligar_motor(self):
        print("Motor ligado.")

class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def esta_carregado(self):
        print("O caminha não esta carregado.")
        
class tanque(Veiculo):
    #sobre escrever o metodo e troca a implementação do metodo pai
    def __init__(self, cor, placa, numero_rodas, carregado=False):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
         print(f'{'Sim'if self.carregado else 'Não'} estou carregado')




moto = Motocicleta('vermelha', 'ABC-1234', 2)
moto.ligar_motor()

carro = Carro('azul', 'DEF-5678', 4)
carro.ligar_motor()
#Se eu fazer igual o caminhao esta carregado
#carro.esta_carregado() vai da error pois são classe diferentes.

Caminhao = Caminhao('preto', 'GHI-9012', 6)
Caminhao.ligar_motor()
Caminhao.esta_carregado()

tanque = tanque('verde', 'JKL-3456', 8, carregado=False)
tanque.esta_carregado()
print(tanque.cor)