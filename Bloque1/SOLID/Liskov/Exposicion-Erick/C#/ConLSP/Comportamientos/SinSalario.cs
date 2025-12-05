using System;

using ConLSP.Interfaces;

namespace ConLSP.Comportamientos
{
    public class SinSalario : IRemunerado
    {
        public decimal CalcularSalario()
        {
            return 0;
        }
    }
}