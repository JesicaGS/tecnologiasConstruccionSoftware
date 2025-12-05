using System;
using SinLSP;

namespace SinLSP;

public class EmpleadoTiempoCompleto : EmpleadoTiempoCompleto
{
    public override decimal CalcularSalario()
    {
        return 3000;
    }

    public override void Trabajar()
    {
        Console.WriteLine("Trabajado 8 horas diarioas");
    }
}