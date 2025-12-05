using system;
using ConLSP.Interfaces;

namespace ConLSP.Comportamientos
{
    public class SalarioFijo : IRemunerado
    {
        private readonly decimal _monto;

        public SalarioFijo(decimal monto)
        {
            _monto = monto;
        }

        public decimal CalcularSalario()
        {
            return _monto;
        }
    }
}