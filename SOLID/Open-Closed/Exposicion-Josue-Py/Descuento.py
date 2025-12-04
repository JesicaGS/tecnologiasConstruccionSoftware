from abc import ABC, abstractmethod

class Descuento(ABC):
    @abstractmethod
    def aplicar(self, precio: float) -> float:
        return precio * 0.70