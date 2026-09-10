from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):    
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass
    
class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligado a TV...")
        print("Ligado!")
        
    def desligar(self):
        print("Desligando a Tv...")
        print("Desligada!")
        
    @property  
    def marca(self):
        return "SAMSUNG"
        
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Lidgado!")
        
    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Ar desligado!")
       
    @property  
    def marca(self):
        return "LG"

controle = ControleTv()
controle.ligar()
controle.desligar()

print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()

print(controle.marca)