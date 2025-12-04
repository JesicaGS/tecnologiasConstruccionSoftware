from DescuentoNavidad import DescuentoNavidad
from DescuentoClienteFrecuente import DescuentoClienteFrecuente
from CalculadoraDescuentos import CalculadoraDescuentos

calc = CalculadoraDescuentos()

print("Navidad: ", calc.calcular(1000, DescuentoNavidad()))
print("Cliente frecuente: ", calc.calcular(1000, DescuentoClienteFrecuente()))