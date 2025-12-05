from Descuento import Descuento

class CalculadoraDescuentos:
    def calcular(self, precio: float, descuento: Descuento) -> float:
        return descuento.aplicar(precio)