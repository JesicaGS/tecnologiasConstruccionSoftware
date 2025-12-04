from abc import ABC, abstractmethod
class Ave(ABC):
    def volar(self):
        pass
    def comer(self):
        pass
    def nadar(self):
        pass

class Aguila(Ave):
    def volar(self):
        print("Aguila está volando...")
    def comer(self):
        print("Aguila está comiendo...")
    def nadar(self):
        raise Exception("Las aguilas no nadan")
    
class Paloma(Ave):
    def volar(self):
        print("Paloma está volando...")
    def comer(self):
        print("Paloma está comiendo...")
    def nadar(self):
        print("Paloma está nadando...")

class Pinguino(Ave):
    def volar(self):
        raise Exception("Los pingüinos no vuelan")
    def comer(self):
        print("Pingüino está comiendo...")
    def nadar(self):
        print("Pingüino está nadando")

a1 = Aguila()
pa1 = Paloma()
p1 = Pinguino()

a1.comer()
a1.volar()
pa1.nadar()
pa1.volar()
p1.volar()
p1.comer()