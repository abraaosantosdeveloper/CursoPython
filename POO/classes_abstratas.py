from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

    @property
    def marca(self):
        pass
    
class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando TV")
        print("Ligada!")
    
    def desligar(self):
        print("Desligando TV")
        print("Desligada!")
        
    def marca(self):
        print("Samsung")
    

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando ar condicionado")
        print("Ligado!")
    
    def desligar(self):
        print("Desligando ar condicionado")
        print("Desligado!")
    
    def marca(self):
        print("LG")
        

controle = ControleTv()
controle.ligar()
controle.desligar()
controle.marca()

arCondicionado = ControleArCondicionado()
arCondicionado.ligar()
arCondicionado.desligar()
arCondicionado.marca()
