using System;

namespace SinLSP;

public class pasante : Empleado
{
    public override decimal CalcularSalario()
    {
        throw new NotImplementedException("Los pasantes no reciben salario");
    }

    public override void Trabajar()
    {
        Console.WriteLine("Aprendiendo y trabajando");
    }
}