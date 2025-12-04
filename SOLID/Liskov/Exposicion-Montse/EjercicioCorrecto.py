from abc import ABC, abstractmethod

class Ave(ABC):
    @abstractmethod
    def comer(self):
        pass
    def respirar(self):
        pass

class AveVoladora(Ave):
    @abstractmethod
    def volar(self):
        pass

class AveNadadora(Ave):
    @abstractmethod
    def nadar(self):
        pass

class Aguila(AveVoladora):
    def comer(self):
        print("Aguila está comiendo...")
    def respirar(self):
        print("Aguila está respirando...")
    def volar(self):
        print("Aguila está volando...")

class Paloma(AveVoladora):
    def comer(self):
        print("Paloma está comiendo")
    def respirar(self):
        print("Paloma está respirando...")
    def volar(self):
        print("Paloma está volando...")

class Pingüino(AveNadadora):
    def comer(self):
        print("Pingüino está comiendo")
    def respirar(self):
        print("Pingüino está respiradno")
    def nadar(self):
        print("Pingüino está nadando")

a1 = Aguila()
pa1 = Paloma()
p1 = Pingüino()

a1.volar()
pa1.respirar()
p1.nadar()
