using ConLSP.Interfaces;

namespace ConLSP.Empleados
{
    public class Pasante : IEmpleado
    {
        public string Nombre { get; }
        public string Puesto { get; } = "Pasante";

        private readonly ITrabajador _trabajador;
        public Pasante(string nombre, ITrabajador trabajador)
        {
            Nombre = nombre;
            _trabajador = trabajador;
        }

        public void Trabajar() => _trabajador.Trabajar();
    }
}