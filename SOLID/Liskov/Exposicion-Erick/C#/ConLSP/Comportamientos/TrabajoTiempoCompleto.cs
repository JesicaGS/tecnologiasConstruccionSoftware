using System;
using ConLSP.Interfaces;

namespace ConLSP.Comportamientos
{
    public class TrabajoTiempoCompleto : ITrabajador
    {
        public void Trabajar()
        {
            Console.WriteLine("Trabajando 8 horas diarias al dia");
        }
    }
}