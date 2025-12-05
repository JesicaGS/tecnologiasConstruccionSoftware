using System;
using ConLSP.Empleados;
using ConLSP.Comportamientos;

namespace ConLSP
{
    public class Program
    {
        public static void Main()
        {
            var sistema = new SistemaNominas();
            var empleado = new EmpleadoRegular
            {
                "Josue",
                "Desarrollador",
                new TrabajoTiempoCompleto(),
                new SalarioFijo(3000)
            };

            var pasante = new Pasante
            {
                "Ricardo",
                new TrabajoPasante()
            };

            Console.WriteLine("Información de empleados: ");
            sistema.MostrarInfo(empleado);
            sistema.MostrarInfo(pasante);

            Console.WriteLine("Traajo asignado: ");
            sistema.AsignarTrabajo(empleado);
            sistema.AsignarTrabajo(pasante);

            Console.WriteLine("Procesando pagos: ");
            sistema.ProcesarPago(empleado);
        }
    }
}