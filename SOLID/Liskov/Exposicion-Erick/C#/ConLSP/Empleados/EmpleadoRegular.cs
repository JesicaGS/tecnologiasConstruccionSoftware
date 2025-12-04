using ConLSP.Interfaces;

namespace ConLSP.Empleados
{
    public class EmpleadoRegular : IEmpleado, IRemunerado
    {
        public string Nombre { get; }
        public string Puesto { get; }

        private readonly ITrabajador _trabajador;
        private readonly IRemunerado _remuneracion;

        public EmpleadoRegular(string nombre, string puesto, ITrabajador trabajador, IRemunerado remuneracion)
        {
            Nombre = nombre;
            Puesto = puesto;
            _trabajador = trabajador;
            _remuneracion = remuneracion;
        }

        public void Trabajar() => _trabajador.Trabajar();

        public decimal CalcularSalario()
        {
            return _remuneracion.CalcularSalario();
        }
    }
}