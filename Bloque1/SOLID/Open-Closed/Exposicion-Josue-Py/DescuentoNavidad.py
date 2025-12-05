from Descuento import Descuento

class DescuentoNavidad(Descuento):
    def aplicar(self, precio: float) -> float:
        return precio * 0.90