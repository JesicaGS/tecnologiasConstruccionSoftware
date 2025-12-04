using System;

namespace ConLSP.Interfaces
{
    public interface IEmpleado : ITrabajador
    {
        string Nombre { get; }
        string Puesto { get; }
    }
}