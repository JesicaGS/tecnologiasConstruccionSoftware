using System;
using ConLSP.Interfaces;

namespace ConLSP
{
    public class SistemaNominas
    {
        public void ProcesarPago(IRemunerado empleado)
        {
            decimal salario = empleado.CalcularSalario();
            Console.WriteLine($"Pago procesado: {salario}");
        }

        public void AsignarTrabajo(ITrabajador trabajador)
        {
            trabajador.Trabajar();
        }

        public void MostrarInfo(IEmpleado empleado)
        {
            Console.WriteLine($"{empleado.Trabajar}");
        }
    }
}