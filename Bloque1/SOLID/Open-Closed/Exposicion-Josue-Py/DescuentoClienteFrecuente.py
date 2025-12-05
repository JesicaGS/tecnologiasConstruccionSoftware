from Descuento import Descuento

class DescuentoClienteFrecuente(Descuento):
    def aplicar(self, precio: float) -> float:
        return precio * 0.80